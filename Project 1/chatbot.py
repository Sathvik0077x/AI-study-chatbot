# chatbot.py

# These are imports — you're loading tools other people built
from openai import OpenAI          # This lets you talk to AI models
print("DEBUG: Script started")
from dotenv import load_dotenv, find_dotenv  # This reads your .env file
import os                          # This lets you access environment variables
import json                        # This lets you save and load chat history

# This line reads your .env file and loads the API key into memory
load_dotenv(find_dotenv(usecwd=True))

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise RuntimeError("Missing GROQ_API_KEY. Add GROQ_API_KEY=your_key_here to your .env file.")

# This creates a "client" — think of it as opening a phone line to the AI
# base_url tells it to use NVIDIA's servers
# api_key is your password to use the service
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=groq_api_key
)

# This is the system prompt — it tells the AI who it is before conversation starts
# You can change this to anything you want
SYSTEM_PROMPT = """You are a helpful study assistant for a final year
computer science student. When explaining concepts, always:
1. Give a simple one-line explanation first
2. Then give a real world example
3. Keep answers short and clear
"""

SAVE_FILE = "chat_history.json"


def fresh_messages():
    return [{"role": "system", "content": SYSTEM_PROMPT}]


def load_messages():
    if not os.path.exists(SAVE_FILE):
        return fresh_messages()

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            saved_messages = json.load(file)

        if not isinstance(saved_messages, list):
            raise ValueError("Saved chat history is not a list.")

        print(f"Loaded saved conversation from {SAVE_FILE}.")
        return saved_messages
    except Exception as e:
        print(f"Could not load saved conversation: {e}")
        print("Starting a fresh conversation.")
        return fresh_messages()


def save_messages(messages):
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=2)


# Print a welcome message
print("=" * 50)
print("AI Study Assistant - Ready!")
print("Type 'save' to save, 'quit' to exit, 'clear' to start fresh")
print("=" * 50)

# This is your conversation history — starts empty
# The system prompt goes in first before any conversation
messages = load_messages()

# This loop runs forever until user types 'quit'
while True:

    # Get input from the user
    user_input = input("\nYou: ").strip()

    # If they typed nothing, ask again
    if not user_input:
        print("Please type something!")
        continue

    # If they type quit, end the program
    if user_input.lower() == "quit":
        print("Goodbye! Good luck with your studies.")
        break

    # If they type clear, reset the conversation
    if user_input.lower() == "clear":
        messages = fresh_messages()
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)
        print("Conversation cleared. Fresh start!")
        continue

    # If they type save, save the conversation to a file
    if user_input.lower() == "save":
        save_messages(messages)
        print(f"Conversation saved to {SAVE_FILE}.")
        continue

    # Add the user's message to conversation history
    messages.append({
        "role": "user",
        "content": user_input
    })

    # This try-except handles errors gracefully
    # Instead of crashing, it prints a friendly message
    try:
        print("\nAI is thinking...")

        # Send the ENTIRE conversation history to the AI
        # This is how it "remembers" — you send everything every time
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",         # The AI model to use
            messages=messages,                       # Full conversation history
            max_tokens=500,                          # Max length of response
            temperature=0.7                          # 0 = robotic, 1 = creative
        )

        # Extract just the text from the response
        reply = response.choices[0].message.content

        # Add AI's response to conversation history
        messages.append({
            "role": "assistant",
            "content": reply
        })

        # Print the response
        print(f"\nAI: {reply}")
        print("-" * 50)

        # Show how many exchanges have happened
        user_messages = len([m for m in messages if m["role"] == "user"])
        print(f"[Exchange #{user_messages}]")

    except Exception as e:
        # If something goes wrong, tell the user what happened
        print(f"Something went wrong: {e}")
        print("Try again!")
