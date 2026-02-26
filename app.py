import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email(data):
    with open("prompts/email_prompt.txt") as f:
        prompt = f.read().format(**data)

    resp = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        response_format={"type": "json_object"}
    )
    return resp.output_json

def generate_resume(data):
    with open("prompts/resume_prompt.txt") as f:
        prompt = f.read().format(**data)

    resp = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        response_format={"type": "json_object"}
    )
    return resp.output_json

# Example
email_data = {
    "sender": "Sachin Kumar",
    "receiver": "HR Team",
    "purpose": "Job application follow-up",
    "points": "Checking status for Software Engineer role",
    "tone": "Professional"
}

print(generate_email(email_data))