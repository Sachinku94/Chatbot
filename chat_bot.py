# simple_chatbot.py
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
client = OpenAI()  # reads OPENAI_API_KEY from env

print("Chatbot ready. Type 'exit' to quit.")
messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user = input("You: ")
    if user.strip().lower() in {"exit", "quit"}: break
    messages.append({"role": "user", "content": user})

    resp = client.chat.completions.create(
        model="gpt-4o-mini",  # cheap & fast; swap to a larger model if you wish
        messages=messages
    )
    reply = resp.choices[0].message.content
    print("Bot:", reply)
    messages.append({"role": "assistant", "content": reply})