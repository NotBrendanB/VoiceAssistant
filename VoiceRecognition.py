import speech_recognition as sr
import time

r = sr.Recognizer()
r.energy_threshold = 50
r.pause_threshold = 1.5

def VoiceReco():

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)

    try:
        audio = r.listen(source, timeout=10, phrase_time_limit=15)

        text = r.recognize_google(audio)
        return text
    except Exception:
        return ""
    