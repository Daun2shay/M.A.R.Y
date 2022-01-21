#f = open("logfile.txt", "a")
#f.write(question '\h')
#f.close()

def storeAnswer(ans):
    filename = "output.txt"
    with open(filename, "w") as f:
        f.write(str(ans))

#def storeQuestion(ques):
