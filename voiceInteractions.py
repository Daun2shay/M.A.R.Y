#!/usr/bin/env python3
# import
import pyttsx3

# do some initialization
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

# testing
engine.say("This is a test!")
engine.say("if you hear this it is a good sign.")
engine.runAndWait()
