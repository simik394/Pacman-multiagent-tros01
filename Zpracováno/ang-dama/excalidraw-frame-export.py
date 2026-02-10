#!/usr/bin/env python3
"""
excalidraw-frame-export.py
Exports a specific frame from an Excalidraw file to a PNG.
Usage: python3 excalidraw-frame-export.py <excalidraw_md> <frame_id> <output_png>
"""

import json
import sys
import re
import os
from pathlib import Path
from typing import Optional, Dict, Any, Tuple

try:
    import lzstring
    HAS_LZSTRING = True
except ImportError:
    HAS_LZSTRING = False
    print("Error: lzstring module not found. Install with: pip install lzstring", file=sys.stderr)
    sys.exit(1)

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("Error: Pillow module not found. Install with: pip install Pillow", file=sys.stderr)
    sys.exit(1)


def decompress_excalidraw(compressed: str) -> Optional[Dict[str, Any]]:
    try:
        lzs = lzstring.LZString()
        decompressed = lzs.decompressFromBase64(compressed)
        if decompressed:
            return json.loads(decompressed)
    except Exception as e:
        print(f"Decompression error: {e}", file=sys.stderr)
    return None


def parse_excalidraw_md(filepath: Path) -> Tuple[Optional[Dict[str, Any]], Dict[str, str]]:
    content = filepath.read_text(encoding='utf-8')
    embedded_files = {}
    
    # Parse embedded file mappings: hash: [[filename]]
    for match in re.finditer(r'^(\w+):\s*\[\[([^\]]+)\]\]', content, re.MULTILINE):
        file_hash, filename = match.groups()
        embedded_files[file_hash] = filename
        
    # Find compressed JSON
    match = re.search(r'```compressed-json\n(.*?)\n```', content, re.DOTALL)
    if match:
        compressed = match.group(1).replace('\n', '')
        data = decompress_excalidraw(compressed)
        return data, embedded_files
    
    return None, embedded_files


def get_frame_crop_info(data: Dict[str, Any], frame_id: str) -> Optional[Dict[str, Any]]:
    elements = data.get('elements', [])
    
    # Find the frame element (by ID or Name)
    frame = next((e for e in elements if e.get('id') == frame_id or e.get('name') == frame_id), None)
    if not frame:
        return None
        
    # Find the FIRST image element (assumption: drawing is annotation over image)
    image = next((e for e in elements if e.get('type') == 'image'), None)
    if not image:
        return None
        
    return {
        'frame_x': frame.get('x', 0),
        'frame_y': frame.get('y', 0),
        'frame_width': frame.get('width', 0),
        'frame_height': frame.get('height', 0),
        'image_x': image.get('x', 0),
        'image_y': image.get('y', 0),
        'image_width': image.get('width', 0),
        'image_height': image.get('height', 0),
        'image_file_id': image.get('fileId'),
    }


def crop_image_to_frame(source_image: Path, output_path: Path, info: Dict[str, Any]) -> bool:
    try:
        img = Image.open(source_image)
        actual_w, actual_h = img.size
        
        # Calculate scale factor (Excalidraw image dimensions vs Actual image pixel dimensions)
        # If Excalidraw says image width is W, but actual pixel width is P, then scale = P / W
        scale_x = actual_w / info['image_width'] if info['image_width'] else 1
        scale_y = actual_h / info['image_height'] if info['image_height'] else 1
        
        # Calculate relative position of frame within the image
        rel_x = info['frame_x'] - info['image_x']
        rel_y = info['frame_y'] - info['image_y']
        
        # Convert to pixel coordinates
        crop_left = int(rel_x * scale_x)
        crop_top = int(rel_y * scale_y)
        crop_right = int((rel_x + info['frame_width']) * scale_x)
        crop_bottom = int((rel_y + info['frame_height']) * scale_y)
        
        # Crop
        cropped = img.crop((
            max(0, crop_left),
            max(0, crop_top),
            min(actual_w, crop_right),
            min(actual_h, crop_bottom)
        ))
        
        cropped.save(output_path, quality=95)
        return True
    except Exception as e:
        print(f"Image processing error: {e}", file=sys.stderr)
        return False


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 excalidraw-frame-export.py <excalidraw_md> <frame_id> <output_png>", file=sys.stderr)
        sys.exit(1)
        
    md_path = Path(sys.argv[1])
    frame_id = sys.argv[2]
    output_path = Path(sys.argv[3])
    
    if not md_path.exists():
        print(f"Error: File not found: {md_path}", file=sys.stderr)
        sys.exit(1)
        
    # 1. Parse Data
    data, embedded_files = parse_excalidraw_md(md_path)
    if not data:
        print(f"Error: Could not parse Excalidraw data from {md_path}", file=sys.stderr)
        sys.exit(1)
        
    # 2. Get Frame Info
    info = get_frame_crop_info(data, frame_id)
    if not info:
        print(f"Error: Frame '{frame_id}' not found or no background image found", file=sys.stderr)
        sys.exit(1)
        
    # 3. Resolve Image Path
    file_id = info['image_file_id']
    image_filename = embedded_files.get(file_id)
    
    source_image = None
    if image_filename:
        # Look in same directory
        check_path = md_path.parent / image_filename
        if check_path.exists():
            source_image = check_path
        else:
            # Fallback: check if basename matches
            pass
            
    if not source_image:
        # Fallback: assume image has same basename as MD (common in some exports)
        # or strip extension
        candidates = [
            md_path.with_suffix('.png'), # file.excalidraw.png
            Path(str(md_path).replace('.excalidraw.md', '.png')), # file.png
            md_path.parent / f"{md_path.stem}.png" # file.excalidraw.png
        ]
        for c in candidates:
            if c.exists():
                source_image = c
                break
                
    if not source_image:
        print(f"Error: Source image not found. Expected file for ID {file_id} ({image_filename})", file=sys.stderr)
        sys.exit(1)
        
    # 4. Crop and Save
    success = crop_image_to_frame(source_image, output_path, info)
    if success:
        print(f"Successfully exported frame {frame_id} to {output_path}")
        sys.exit(0)
    else:
        print("Failed to export frame", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
