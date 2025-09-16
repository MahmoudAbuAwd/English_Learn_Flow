# test_gemini_env.py
import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Read API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Init client
client = genai.Client(api_key=api_key)

# Test call
resp = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="hi"
)

print("=== Gemini response ===")
print(resp.text)
