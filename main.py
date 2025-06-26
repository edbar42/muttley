import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("API_KEY")
client = genai.Client(api_key=api_key)

try:
    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    print(
        f"Prompt tokens: {response.usage_metadata.prompt_token_count}",
        f"Response tokens: {response.usage_metadata.candidates_token_count}",
        response.text,
        sep="\n"
    )

except IndexError:
    print("No argument was given. Try again.")
    exit(1)
