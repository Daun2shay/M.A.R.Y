def storeAnswer(ans):
    filename = "output.txt"
    with open(filename, "a" ) as f:
        f.write(str(ans))