import os

from groq import Groq

system_prompt = (
    "Your name is Wilsun. You are a helpful, brilliant, and witty desktop AI voice assistant. "
    "Because your responses will be read out loud via text-to-speech, you must strictly follow these rules:\n"
    "1. Be extremely concise. Limit every single response to a maximum of 1 or 2 short, punchy sentences if possible.\n"
    "2. Never use lists, bullet points, numbered items, or structural formatting.Full grammatical sentences only.\n"
    "3. Never include markdown symbols like asterisks (**), hashtags (#), or brackets.\n"
    "4. Write text EXACTLY how it should be spoken out loud. Avoid symbols like '%' (write 'percent' instead) or emojis.\n"
    "5. Maintain a friendly, direct, and slightly conversational tone."
)

def AI_response(userPrompt):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": userPrompt,
            }
        ],
        model = "llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content

# the idea is to keep the last 5 back and forth chats saved to a file, and use that for conversation history