import speech_recognition as sr
import time

r = sr.Recognizer()
r.energy_threshold = 50
r.pause_threshold = 1

def VoiceReco():

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=15)

            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Couldn't Understand Words")
            return ""
        except Exception as e:
            print(f"ERROR: {e}")
            return ""