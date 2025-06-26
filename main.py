import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("API_KEY")
client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=sys.argv[1]
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
