#!/usr/bin/env python3
import datetime;


def whatTime():
    print("Yes!")
    localtime = datetime.datetime.now()
    print("Local current time " + localtime.strftime("%Y-%m-%d %H:%M:%S"))

def calcMult():
    print("Yes")
    op1 = int(input('Please enter operator 1: '))
    op2 = int(input('Please enter operator 2: '))
    answer = op1*op2
    print("The answer is : " + str(answer))

def default():
    print("Not an available question.")

def switch(operation):
    dict={
        'what time is it?': whatTime,
        'can you multiply two numbers?': calcMult,
    }
    return dict.get(operation, default)()

operation = input('Please ask M.A.R.Y. a question: ')
switch(operation)
