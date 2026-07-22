import asyncio

from VoiceRecognition import VoiceReco
from AIConnection import AI_response
from TextToSpeech import text_to_speech

async def brain():

    userInput = VoiceReco()
    print("done with voice rec., send to ai")
    aiOutput = AI_response(userInput)
    print("got response from ai, send to tts")
    await text_to_speech(aiOutput)

asyncio.run(brain())