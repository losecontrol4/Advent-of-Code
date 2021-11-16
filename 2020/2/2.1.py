numMin = []
numMax = []
letter = []
password = []


def parseFile(fileName):
    f = open(fileName, 'r')
    for line in f.readlines():
        brokenLine = line.split(" ")
        password.append(brokenLine[2])
        letter.append(brokenLine[1][0])
        brokenLine = brokenLine[0].split("-")
        numMin.append(int(brokenLine[0]))
        numMax.append(int(brokenLine[1]))
    return


def answer():
    parseFile("input.txt")
    validPasswords = 0
    for i in range(len(numMin)):
        letterCount = password[i].count(letter[i])
        if(letterCount >= numMin[i] and letterCount <= numMax[i]):
            validPasswords += 1
    return validPasswords


print(answer())
