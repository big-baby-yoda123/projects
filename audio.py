import os
import time
from winsound import PlaySound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3



def speak(voice):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.say(voice)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            pass
            #print("Exception: " + str(e))
    return said
