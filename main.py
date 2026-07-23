import asyncio
import customtkinter as ctk
import threading

from VoiceRecognition import VoiceReco
from AIConnection import AI_response
from TextToSpeech import text_to_speech


app = ctk.CTk()
app.geometry("1920x1080")
app.title("Wilsun")
app.configure(fg_color="#d8d0c5")

ctk.set_appearance_mode("Dark")

def brain():
    app.after(0, updateResponseText, "Listening...")
    userInput = VoiceReco()

    app.after(0, updateResponseText, "Thinking...")
    aiOutput = AI_response(userInput)

    app.after(0, updateResponseText, aiOutput)
    asyncio.run(text_to_speech(aiOutput))

def startEvent():
    threading.Thread(target=brain, daemon=True).start()

AIText = "Say Something, Get Started!"

startButton = ctk.CTkButton(app, text="Begin Voice Prompt", command=startEvent, fg_color = "#362c23",
                            height=50)
titleText = ctk.CTkLabel(app, text="Wilsun", text_color = "#362c23",
                          fg_color="transparent",font=("Georgia", 250))
responseText = ctk.CTkLabel(app, text=AIText, fg_color="white", width=800, text_color="#362c23",
                            font=("Times New Roman", 32), wraplength=700, justify="left")

responseText.pack(side="right", fill="y", pady=20, padx=20)
titleText.pack(side="top", anchor="w", pady=200, padx=150)
startButton.pack(side="top", anchor="w", padx=450)

def updateResponseText(changedText):
    responseText.configure(text=changedText)

app.mainloop()