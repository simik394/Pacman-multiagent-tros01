import json
import sys
import re

def parse_board(table_text):
    # Extract cells with pieces
    # Table indicates positions 1-32.
    # Usually the markdown table maps visually.
    # I'll just look for cells containing symbols.
    pieces = []
    rows = table_text.strip().split('\n')
    # Skip header and separator
    current_row = 0
    for line in rows:
        if '---' in line: continue
        if not line.startswith('|'): continue
        
        cells = [c.strip() for c in line.strip().split('|') if c]
        for cell in cells:
            if '🔴' in cell:
                pieces.append(f"Red: {cell}")
            if '⚫' in cell:
                pieces.append(f"Black/White: {cell}")
            # Also capture number if present with piece
    return ", ".join(pieces)

def extract_nodes_in_groups(canvas_path):
    with open(canvas_path, 'r') as f:
        data = json.load(f)
    
    nodes = data.get('nodes', [])
    groups = [n for n in nodes if n.get('type') == 'group']
    text_nodes = [n for n in nodes if n.get('type') == 'text']

    for group in groups:
        gx, gy = group['x'], group['y']
        gw, gh = group['width'], group['height']
        label = group.get('label', 'Unnamed Group')
        
        print(f"Group: {label}")
        
        # Find nodes inside this group
        contained_texts = []
        for node in text_nodes:
            nx, ny = node['x'], node['y']
            nw, nh = node['width'], node['height']
            cx, cy = nx + nw/2, ny + nh/2
            if gx <= cx <= gx + gw and gy <= cy <= gy + gh:
                contained_texts.append(node.get('text', '').strip())

        for text in contained_texts:
            if text.startswith('|'):
                 p = parse_board(text)
                 print(f"  - Board: {p}")
            else:
                 print(f"  - Note: {text[:50]}...")

if __name__ == "__main__":
    extract_nodes_in_groups(sys.argv[1])
