#!/usr/bin/env python3
from voiceInteractions import *
from log import *
from PyDictionary import PyDictionary
import datetime;
import random;

# Area to store the various responses M.A.R.Y. will call depending on where the user is

# Generic initial greeting list
gResponseList = ["Please ask MARY a question: ",
    "Hi! I'm M.A.R.Y. ask me any question! ",
    "Welcome to the Movie-like Artificial-inteligence RepositorY AKA MARY\nPlease ask the system a question: ",
    "Hello, ask a question and you shall receive your answer: ",
    "You've started MARY, please enter a question: "]

# Generic question unavailable responses
qUnavailResponse = ["Not an available question.",
    "Unfortunately, MARY does not support that question yet.",
    "Our developers are currently hard at work to add this question to our system.\nSadly, I cannot answer it yet.",
    "I cannot answer that question yet, please ask me something else!"]

qAvailResponse = ["Yes!",
    "Absolutely I can!",
    "You have asked, and so I shall answer",
    "Processing.....",
    "Accessing MARY database..."]

# Part that takes the input and takes you to a question
def startPrompt():
    prompt = random.choice(gResponseList)
    sayText(prompt)
    question = input(prompt)
    questionSwitch(question)
