import asyncio
import edge_tts

text = "Hi there! I am your voice assistant. How can I help you today?"
voice = "en-US-AndrewNeural"
output_file = "output.mp3"

async def text_to_speech() -> None:
    """Main function"""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

if __name__ == "__main__":
    asyncio.run(text_to_speech())

