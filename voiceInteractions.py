#!/usr/bin/env python3
# import
import pyttsx3

# do some initialization
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

# testing
def sayText(text):
    engine.say(text)
    engine.runAndWait()
