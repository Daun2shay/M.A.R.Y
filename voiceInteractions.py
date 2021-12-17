#!/usr/bin/env python3
# import
import pyttsx3
import speech_recognition as sr

# do some initialization
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print('Talk')
    r.adjust_for_ambient_noise(source)
    audio_text = r.listen(source)
    print("Time over, thanks")

try:
    print("Text: " + r.recognize_google(audio_text))
except:
    print("Sorry, I did not get that.")

engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

# testing
def sayText(text):
    engine.say(text)
    engine.runAndWait()
