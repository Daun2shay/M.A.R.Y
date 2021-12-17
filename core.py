#!/usr/bin/env python3
import datetime;
import random;
import pyttsx3;
import speech_recognition as sr;

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Area to store the various responses M.A.R.Y. will call depending on where the user is

# Generic initial greeting list
gResponseList = ["Please ask M.A.R.Y. a question: ",
    "Hi! I'm M.A.R.Y. ask me any question! ",
    "Welcome to the Movie-like Artificial-inteligence RepositorY AKA M.A.R.Y.\nPlease ask the system a question: ",
    "Hello, ask a question and you shall receive your answer: ",
    "You've started M.A.R.Y., please enter a question: "]

# Generic question unavailable responses
qUnavailResponse = ["Not an available question.",
    "Unfortunately, M.A.R.Y. does not support that question yet.",
    "Our developers are currently hard at work to add this question to our system.\nSadly, I cannot answer it yet.",
    "I cannot answer that question yet, please ask me something else!"]

qAvailResponse = ["Yes!",
    "Absolutely I can!",
    "You have asked, and so I shall answer",
    "Processing.....",
    "Accessing M.A.R.Y. database..."]

# Different questions
# Function for what the current time is
def whatTime():
    print(random.choice(qAvailResponse))
    localtime = datetime.datetime.now()
    print("Local current time " + localtime.strftime("%Y-%m-%d %H:%M:%S"))

# Function for calculating 2 digit multiplication
def calcMult():
    print(random.choice(qAvailResponse))
    op1 = int(input('Please enter operator 1: '))
    op2 = int(input('Please enter operator 2: '))
    answer = op1*op2
    print("The answer is : " + str(answer))

# Response to an unavailable question
def default():
    print(random.choice(qUnavailResponse))

# Function to handle the different questions
def questionSwitch(question):
    questions={
        'what time is it?': whatTime,
        'can you multiply two numbers?': calcMult,
    }
    return questions.get(question, default)()

# Part that takes the input and takes you to a question
question = input(random.choice(gResponseList))
questionSwitch(question)

# Part that logs user input to a file
f = open('LogFile.txt', 'a')
f.write(question + "\n")
f.close()