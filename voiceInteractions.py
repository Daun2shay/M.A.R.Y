#!/usr/bin/env python3
# import
import pyttsx3
import speech_recognition as sr
import time

# do some initialization

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception " + str(e))

    return said.lower()

r = sr.Recognizer()
mic = sr.Microphone()

def voiceToVar():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio_text = r.listen(source)
        return r.recognize_google(audio_text)


# testing
def sayText(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    engine.say(text)
    engine.runAndWait()
