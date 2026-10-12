from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
notes = """FastAPI makes it quick to build APIs in Python.
You can define routes with decorators like @app.get("/").
Type hints help validate inputs and shape responses.
It generates interactive API docs automatically.
I learned that async endpoints can handle waiting efficiently.
Pydantic models keep request data organized.
There’s still plenty to learn about deployment and testing."""
client = genai.Client(api_key=gemini_api_key)
def summarize(notes, instructions):
    try:
        prompt = f"{instructions}\n\nNotes:\n{notes}"
        response = client.models.generate_content(model="gemini-3.5-flash-lite", contents=prompt)
        

        return response.text
        
    
    except Exception as e:
        return f"An error occurred: {e}"
a=summarize(notes, "Summarize the following notes in a few sentences.")
b=summarize(notes, "Summarize this conncept to me within 50 words,with  headliine and bullet points.")
print("--- A: vague ---")
print(a)
print("--- B: specific ---")
print(b)