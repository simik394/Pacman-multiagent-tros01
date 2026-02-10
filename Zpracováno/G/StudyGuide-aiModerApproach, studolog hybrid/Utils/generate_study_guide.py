import os
import requests
import json
import time
import re

# Configuration
INPUT_DIR = "/home/sim/Obsi/Prods/04-škola/Předměty/mgr3/4IZ431 AI1/Study_Guide_Tasks"
OUTPUT_DIR = "/home/sim/Obsi/Prods/04-škola/Předměty/mgr3/4IZ431 AI1/Study_Guide_Output"
RSRCH_ENDPOINT = "http://halvarm:3030/v1/chat/completions"
MODEL = "gemini-deep-research" # Use the model capable of reasoning/synthesis

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def process_lesson(filename):
    input_path = os.path.join(INPUT_DIR, filename)
    lesson_id = filename.replace("Task_Lesson_", "").replace(".txt", "")
    output_path = os.path.join(OUTPUT_DIR, f"Lesson_{lesson_id}.md")
    
    if os.path.exists(output_path):
        print(f"Skipping {lesson_id} (already exists)")
        return

    print(f"Processing {lesson_id}...")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        prompt_content = f.read()

    # The prompt content is huge (Lesson + Book). 
    # We send it to Rsrch Agent.
    
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert AI tutor. Output in Czech Markdown."},
            {"role": "user", "content": prompt_content}
        ],
        "temperature": 0.3
    }

    try:
        start_time = time.time()
        response = requests.post(RSRCH_ENDPOINT, json=payload, timeout=600) # 10 min timeout
        response.raise_for_status()
        
        result = response.json()
        content = result['choices'][0]['message']['content']
        
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(content)
            
        elapsed = time.time() - start_time
        print(f"✓ Finished {lesson_id} in {elapsed:.1f}s")
        
    except Exception as e:
        print(f"❌ Failed {lesson_id}: {e}")

def main():
    files = sorted([f for f in os.listdir(INPUT_DIR) if f.startswith("Task_Lesson_")])
    
    print(f"Found {len(files)} lessons to process.")
    print(f"Target: {RSRCH_ENDPOINT}")
    
    for f in files:
        process_lesson(f)

if __name__ == "__main__":
    main()
