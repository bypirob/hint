import os
import requests
import sys
import json
from dotenv import load_dotenv

def claude_provider(prompt):
    url = "https://api.anthropic.com/v1/messages"
    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 100,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    res = requests.post(url, json=data, headers={
        "x-api-key": os.getenv("ANTHROPIC_API_KEY"),
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    })

    data = json.loads(res.text)
    text_output = data['content'][0]['text']

    return text_output


def generate_command(description):
    prompt = f"""
    Generate the terminal command for the following description without any explanations or additional text:
    
    {description}
    """

    command = claude_provider(prompt)

    return command

def main():
    description = " ".join(sys.argv[1:])
    command = generate_command(description)

    print(f"> command: {command}")

if __name__ == "__main__":
    load_dotenv()
    main()