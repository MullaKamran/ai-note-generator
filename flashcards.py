import json
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=gemini_api_key)
def get_study_material(notes):
    prompt = f"""
    Using only the notes below, create study material.

    Return JSON in exactly this shape:
    {{
    "flashcards": [{{"question": "Capital of France", "answer": "Paris"}}],
    "quiz": [{{"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Madrid"], "correct_index": 2}}]
    }}

    Rules:
    - Exactly 3 flashcards and 3 quiz questions.
    - Each quiz question has exactly 4 options.
    - correct_index is a number (0 to 3), not a string.
    - Return only raw JSON, no markdown.

    Notes:
    {notes}
    """
    try:
        response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
            )
        data = json.loads(response.text)   
        return data
    except json.JSONDecodeError:
        print("Model didn't return valid JSON")            
        return None
notes = """FastAPI is a Python framework for building APIs quickly.
It uses type hints to validate data and define responses.
It automatically creates interactive API documentation.
It supports both regular and asynchronous routes.
Overall, it makes API development clear and efficient."""
    
    
result = get_study_material(notes)

if result:
    for card in result["flashcards"]:
        print("Q:", card["question"])
        print("A:", card["answer"])

    for item in result["quiz"]:
        print(item["question"])
        for i, option in enumerate(item["options"], start=1):
            print(f"  {i}. {option}")
        print("Correct answer:", item["options"][item["correct_index"]])
            