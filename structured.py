import json
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=gemini_api_key)
def get_structured_notes(notes):
    prompt = f"""
    Summarize the notes below. Use only information from the notes.

    Return JSON in exactly this shape:
    {{"summary": "...", "key_points": ["...", "..."]}}

    Return only raw JSON, no markdown.

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
result = get_structured_notes(notes)

if result:
    print(result["summary"])
    for point in result["key_points"]:
        print("-", point)