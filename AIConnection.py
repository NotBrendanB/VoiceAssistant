import os

from groq import Groq

def AI_response(userPrompt):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "user",
                "content": userPrompt, 
            }
        ],
        model = "llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content

# the idea is to keep the last 5 back and forth chats saved to a file, and use that for conversation history