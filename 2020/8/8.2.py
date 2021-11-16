from os import openpty


acc = 0
code = []
testedLines = set()


def getCode(fileName):
    f = open(fileName, 'r')
    global code
    code = f.readlines()
    f.close()


def runCode(test):
    global acc
    global code
    lineNum = 0
    # oldLineNum = 0  # marks line before last jump or nop
    while(True):
        if(lineNum >= len(code)):
            return

        line = code[lineNum]
        # print(line)
        opp = line.split()[0]
        arg = line.split()[1]
        code[lineNum] = "ne in"
        if(opp == "nop"):
            if(test and not lineNum in testedLines):
                testedLines.add(lineNum)
                return lineNum
            lineNum += 1
        elif(opp == "jmp"):
            if(test and not lineNum in testedLines):
                testedLines.add(lineNum)
                return lineNum
            #oldLineNum = lineNum
            lineNum += int(arg)
        elif(opp == "acc"):
            lineNum += 1
            acc += int(arg)
        else:
            return lineNum  # value not used anymore, just in for a check that a value did return


def bugTest():
    global code
    global acc
    while(True):
        acc = 0
        getCode("input.txt")

        testLine = runCode(True)

        getCode("input.txt")
        acc = 0

        line = code[testLine]
        # print(testedLines)
        opp = line.split()[0]
        arg = line.split()[1]
        if(opp == "jmp"):
            code[testLine] = "nop " + arg + "\n"
        if(opp == "nop"):
            code[testLine] = "jmp " + arg + "\n"
       # print("—————————————————————")
        # print(code[testLine])
        # print("—————————————————————")
        if(runCode(False) == None):
            return acc


print(bugTest())
