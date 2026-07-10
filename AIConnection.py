import os

print("YOUR CURRENT KEY IS:", os.environ.get("GROQ_API_KEY"))

from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": "Explain the importance of fast language models", 
        }
    ],
    model = "llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)

# the idea is to keep the last 5 back and forth chats saved to a file, and use that for conversation history