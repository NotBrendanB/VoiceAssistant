import asyncio
import edge_tts
import pygame
import io


async def text_to_speech(text) -> None:
    pygame.mixer.init()
    
    stream = io.BytesIO()
    communicator = edge_tts.Communicate(text, "en-US-AndrewNeural")

    async for chunk in communicator.stream():
        if chunk["type"] == "audio":
            stream.write(chunk["data"])

    stream.seek(0)

    pygame.mixer.music.load(stream)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)
    
    pygame.mixer.quit()
    stream.close()

