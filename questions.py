from voiceInteractions import *
from log import *
from PyDictionary import PyDictionary
import datetime;
import random;

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
    sayText(resp)
    print(resp)
    sayText('Please enter operator 1: ')
    op1 = int(input('Please enter operator 1: '))
    sayText('Please enter operator 2: ')
    op2 = int(input('Please enter operator 2: '))
    answer = op1*op2
    answerString = "The answer is : " + str(answer)
    sayText(answerString)
    print(answerString)
    storeAnswer(answerString)

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
        storeAnswer(word[state])
        print(word[state])
        sayText('The meaning of the word is' + str(word[state]))

# Response to an unavailable question
def default():
    qUnavailString = random.choice(qUnavailResponse)
    sayText(qUnavailString)
    print(qUnavailString)
    storeAnswer(qUnavailString)

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
