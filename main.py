import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <prompt>")
        print("Try passing in a message in double quotes when you call this script.")
        sys.exit(1)

    prompt = sys.argv[1]

    load_dotenv()
    api_key = os.environ.get("API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        print(
            f"User prompt: {messages[-1].parts[-1].text}",
            f"Prompt tokens: {response.usage_metadata.prompt_token_count}",
            f"Response tokens: {
                response.usage_metadata.candidates_token_count}",
            response.text,
            sep="\n"
        )
    else:
        print(response.text)


if __name__ == "__main__":
    main()
