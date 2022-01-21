#!/usr/bin/env python3
# import
import pyttsx3
import speech_recognition as sr

# do some initialization
r = sr.Recognizer()
mic = sr.Microphone()

def voiceToVar():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio_text = r.listen(source)
        return r.recognize_google(audio_text)

engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

# testing
def sayText(text):
    engine.say(text)
    engine.runAndWait()
