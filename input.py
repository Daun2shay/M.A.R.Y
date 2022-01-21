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

# Different questions
# Function for what the current time is
def whatTime():
    resp = random.choice(qAvailResponse)
    sayText(resp)
    print(resp)
    localtime = datetime.datetime.now()
    timeString = "Local current time is " + localtime.strftime("%Y-%m-%d %H:%M")
    sayText(timeString)
    print(timeString)

# Function for calculating 2 digit multiplication
def calcMult():
    resp = random.choice(qAvailResponse)
    sayText(resp)
    print(resp)
    sayText('Please enter operator 1: ')
    op1 = int(input('Please enter operator 1: '))
    storeAnswer(op1)
    sayText('Please enter operator 2: ')
    op2 = int(input('Please enter operator 2: '))
    answer = op1*op2
    answerString = "The answer is : " + str(answer)
    sayText(answerString)
    print(answerString)

# Function for defining words
def wordDefine():
    dic = PyDictionary()
    resp = random.choice(qAvailResponse)
    sayText(resp)
    print(resp)
    sayText('Please tell me the word you would like me to define: ')
    print('Please tell me the word you would like me to define: ')
    query = str(input())
    word = dic.meaning(query)

    for state in word:
        print(word[state])
        sayText('The meaning of the word is' + str(word[state]))

# Response to an unavailable question
def default():
    qUnavailString = random.choice(qUnavailResponse)
    sayText(qUnavailString)
    print(qUnavailString)

# Function to handle the different questions
def questionSwitch(question):
    questions={
        'what time is it': whatTime,
        'can you multiply two numbers': calcMult,
        'can you define a word': wordDefine,
    }
    return questions.get(question, default)()

# Part that takes the input and takes you to a question
def startPrompt():
    prompt = random.choice(gResponseList)
    sayText(prompt)
    question = input(prompt)
    questionSwitch(question)
