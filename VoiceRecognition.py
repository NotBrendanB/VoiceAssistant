import speech_recognition as sr
import time

running = True

r = sr.Recognizer()

def callback(recognizer, audio):
    global running
    try:
        text = recognizer.recognize_google(audio)
        if text == "stop":
            running = False 
        else:
            print("You said : " + text)
    except:
        print("Error")

source = sr.Microphone()
r.energy_threshold = 50
stop_listening = r.listen_in_background(source, callback)

while running:
    time.sleep(1)