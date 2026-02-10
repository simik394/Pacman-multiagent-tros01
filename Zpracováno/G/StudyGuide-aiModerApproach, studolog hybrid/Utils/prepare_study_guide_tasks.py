import os
import re
from pypdf import PdfReader

# Configuration
LESSON_NOTES_FILE = "/home/sim/Obsi/Prods/04-škola/Předměty/mgr3/4IZ431 AI1/lesson_notes_full.txt"
CHAPTERS_DIR = "/home/sim/Obsi/Prods/04-škola/Předměty/mgr3/4IZ431 AI1/Chapters"
OUTPUT_DIR = "/home/sim/Obsi/Prods/04-škola/Předměty/mgr3/4IZ431 AI1/Study_Guide_Tasks"

# Mapping: Lesson Number (String) -> List of Chapter Filename Patterns
MAPPING = {
    "01": ["1_Introduction", "26_Philosophical_Foundations"],
    "02": ["2_Intelligent_Agents", "26_Philosophical_Foundations"],
    "03": ["3_Solving_Problems_by_Searching", "4_Beyond_Classical_Search"],
    "04": ["6_Constraint_Satisfaction_Problems", "7_Logical_Agents"],
    "05": ["5_Adversarial_Search"],
    "06": ["10_Classical_Planning", "4_Beyond_Classical_Search"],
    "07": ["18_Learning_from_Examples"],
    "08": ["19_Knowledge_in_Learning", "12_Knowledge_Representation"],
    "09": ["21_Reinforcement_Learning", "17_Making_Complex_Decisions"],
    "10": ["24_Perception"],
    "11": ["25_Robotics", "2_Intelligent_Agents"]
}

def parse_lesson_notes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by header pattern like "01 - " or "11 - "
    # We look for start of line, digit, digit, space, hyphen
    sections = {}
    pattern = re.compile(r'^(\d{2}) - (.*)$', re.MULTILINE)
    
    matches = list(pattern.finditer(content))
    
    for i, match in enumerate(matches):
        lesson_num = match.group(1)
        lesson_title = match.group(2).strip()
        start_idx = match.end()
        
        # End index is the start of the next match, or end of file
        end_idx = matches[i+1].start() if i+1 < len(matches) else len(content)
        
        text = content[start_idx:end_idx].strip()
        sections[lesson_num] = {
            "title": lesson_title,
            "content": text
        }
    return sections

def get_pdf_text(chapter_name_pattern):
    # Find the actual filename
    for fname in os.listdir(CHAPTERS_DIR):
        if chapter_name_pattern in fname:
            full_path = os.path.join(CHAPTERS_DIR, fname)
            try:
                reader = PdfReader(full_path)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text
            except Exception as e:
                print(f"Error reading {full_path}: {e}")
                return ""
    print(f"Warning: Chapter matching '{chapter_name_pattern}' not found.")
    return ""

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    print("Parsing lesson notes...")
    lessons = parse_lesson_notes(LESSON_NOTES_FILE)
    
    print(f"Found {len(lessons)} lessons.")
    
    for lesson_num, data in lessons.items():
        print(f"Processing Lesson {lesson_num}: {data['title']}...")
        
        # 1. Get Lesson Text
        lesson_text = data['content']
        
        # 2. Get Book Context
        book_context = ""
        chapter_patterns = MAPPING.get(lesson_num, [])
        for pattern in chapter_patterns:
            print(f"  - extracting text from chapter: {pattern}")
            chapter_text = get_pdf_text(pattern)
            book_context += f"\n\n--- BOOK CHAPTER: {pattern} ---\n\n{chapter_text}"
            
        # 3. Create Prompt File
        output_filename = os.path.join(OUTPUT_DIR, f"Task_Lesson_{lesson_num}.txt")
        
        prompt = f"""
START_INSTRUCTION
You are an expert AI tutor creating a comprehensive study guide.
Your task is to rewrite and expand the "Lesson Notes" provided below into a cohesive, readable study text.

1. **Structure:** Follow the exact structure and order of the topics in the "Lesson Notes". Do not reorder them.
2. **Enrichment:** Use the "Textbook Context" provided to expand on every bullet point in the notes.
    - If the notes mention a concept (e.g., "Rationality"), define it precisely using the textbook.
    - If the notes list algorithms (e.g., "A*", "Simulated Annealing"), explain how they work, their complexity, and pros/cons using the textbook details.
    - Add examples from the textbook where appropriate.
3. **Tone:** Academic but accessible study material. Not just bullet points—write paragraphs where necessary to explain complex ideas.
4. **Language:** The output must be in **Czech** (since the lesson notes are in Czech), but you can keep standard English AI terminology (like "Overfitting") in parentheses.

--- LESSON NOTES (Skeleton) ---
{data['title']}

{lesson_text}

--- TEXTBOOK CONTEXT (Source Material) ---
{book_context}

END_INSTRUCTION
"""
        with open(output_filename, 'w', encoding='utf-8') as out:
            out.write(prompt)
            
    print(f"Done. Task files generated in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
