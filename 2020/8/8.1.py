from os import openpty


acc = 0
code = []


def getCode(fileName):
    f = open(fileName, 'r')
    global code
    code = f.readlines()
    f.close()


def runCode():
    lineNum = 0
    while(True):
        global acc
        global code
        line = code[lineNum]
        opp = line.split()[0]
        arg = line.split()[1]
        code[lineNum] = "ne in"
        if(opp == "nop"):
            lineNum += 1
        elif(opp == "jmp"):
            lineNum += int(arg)
        elif(opp == "acc"):
            lineNum += 1
            acc += int(arg)
        else:
            return acc


getCode("input.txt")
print(runCode())
