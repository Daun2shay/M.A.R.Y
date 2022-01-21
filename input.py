#!/usr/bin/env python3
from voiceInteractions import *
from log import *
from PyDictionary import PyDictionary
import datetime;
import random;
import operator


# Area to store the various responses M.A.R.Y. will call depending on where the user is
#######################################################################################
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

# Generic responses for available question
qAvailResponse = ["Yes!",
    "Absolutely I can!",
    "You have asked, and so I shall answer",
    "Processing.....",
    "Accessing MARY database..."]

# Different functions for M.A.R.Y. to answer
#######################################################################################
# Function for what the current time is
def whatTime():
    resp = random.choice(qAvailResponse)
    sayText(resp)
    print(resp)
    localtime = datetime.datetime.now()
    timeString = "Local current time is " + localtime.strftime("%Y-%m-%d %H:%M")
    sayText(timeString)
    print(timeString)
    storeAnswer(timeString)

# Function for calculating 2 digit multiplication
def calcMult():
    resp = random.choice(qAvailResponse)
    print(resp)
    sayText(resp)
    print('Please tell me your calculation: ')
    sayText('Please tell me your calculation: ')

    operation = voiceToVar()
    print(operation)

    def getOperatorFn(op):
        return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        '*' : operator.mul,
        'divided' : operator.__truediv__,
        '/' : operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]

    def evalBinaryExpr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return getOperatorFn(oper) (op1, op2)

    answer = evalBinaryExpr(*(operation.split()))

    answerString = "The answer is : " + str(answer)
    print(answerString)
    sayText(answerString)
    storeAnswer(answerString)

# Function for defining words
def wordDefine():
    dic = PyDictionary()
    resp = random.choice(qAvailResponse)
    sayText(resp)
    print(resp)
    sayText('Please tell me the word you would like me to define: ')
    print('Please tell me the word you would like me to define: ')
    query = str(voiceToVar)
    word = dic.meaning(query)

    for state in word:
        storeAnswer(word[state])
        print(word[state])
        sayText('The meaning of the word is' + str(word[state]))

# Response to an unavailable question
def default():
    qUnavailString = random.choice(qUnavailResponse)
    sayText(qUnavailString)
    print(qUnavailString)
    storeAnswer(qUnavailString)

# Handling the prompts and question
################################################################################
# Function to handle the different questions
def questionSwitch(question):
    questions={
        'what time is it': whatTime,
        'can you perform a calculation': calcMult,
        'can you define a word': wordDefine,
    }
    return questions.get(question, default)()

# Start of the program
################################################################################
# Part that takes the input and takes you to a question
def startPrompt():
    prompt = random.choice(gResponseList)
    sayText(prompt)
    print(prompt)
    question = voiceToVar()
    print(question)
    questionSwitch(question)
