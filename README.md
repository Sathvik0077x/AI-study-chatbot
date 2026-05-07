# AI Chatbot With Memory

A command-line AI chatbot built using Python and Groq's LLM API.
The chatbot maintains conversation memory by storing and resending the full message history with every API request.

---

# Features

* Conversational AI chatbot
* Memory-based conversation handling
* System prompt customization
* Conversation reset feature
* Save conversation to text file
* Error handling using try-except
* Context window trimming for performance optimization

---

# Technologies Used

* Python
* OpenAI Python SDK
* Groq API
* dotenv

---

# Project Structure

```bash
project1-chatbot/
│
├── chatbot.py
├── .env
├── README.md
└── conversation_saved.txt
```

---

# How Memory Works

LLMs do not have built-in memory between API calls.

This chatbot creates memory by storing the entire conversation in a `messages` list and sending the full history with every new request.

Example:

```python
messages = [
    {"role": "user", "content": "My name is Sathvik"},
    {"role": "assistant", "content": "Nice to meet you!"},
    {"role": "user", "content": "What is my name?"}
]
```

Because previous messages are included, the AI can answer contextually.

---

# Installation

## 1. Clone the Repository

```bash
git clone your-github-repo-link
cd project1-chatbot
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install openai python-dotenv
```

---

# API Key Setup

Create a `.env` file in the project root folder.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

---

# Running the Project

```bash
python chatbot.py
```

---

# Available Commands

| Command | Function                       |
| ------- | ------------------------------ |
| `quit`  | Exit chatbot                   |
| `clear` | Reset conversation memory      |
| `save`  | Save conversation to text file |

---

# Example Conversation

```text
You: My name is Sathvik

AI: Nice to meet you Sathvik!

You: What is my name?

AI: Your name is Sathvik.
```

---

# Save Feature

Typing:

```text
save
```

creates a text file containing the conversation history.

---

# Concepts Learned

This project demonstrates:

* API integration
* Conversation state management
* Context replay
* Prompt engineering
* Error handling
* File handling
* Environment variable management

---

# Error Handling

The chatbot uses `try-except` blocks to prevent crashes during:

* API failures
* Invalid keys
* Internet issues
* Rate limits

---

# Future Improvements

Possible upgrades:

* Web interface using Flask/FastAPI
* Voice input/output
* Database storage
* Streaming responses
* User authentication
* Vector database memory
* RAG integration

---

# Key Learning

The most important concept learned in this project:

> LLMs are stateless. Memory is created by replaying previous conversation context with every API request.

---

# Author

Sathvik
