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
    f.close()
    return


def answer():
    parseFile("input.txt")
    validPasswords = 0
    for i in range(len(numMin)):
        if((password[i][numMin[i] - 1] == letter[i]) != (password[i][numMax[i] - 1] == letter[i])):
            validPasswords += 1
    return validPasswords


print(answer())
