from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)
try:
    response = client.models.generate_content(model="gemini-3.5-flash-lite", contents="Write a short poem about the ocean.")
    print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")
