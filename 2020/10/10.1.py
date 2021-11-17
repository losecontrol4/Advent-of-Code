volts = []


def getVolts(fileName):
    global volts
    f = open(fileName, 'r')
    volts = f.read().split("\n")
    for i in range(len(volts)):
        volts[i] = int(volts[i])
    volts.append(0)
    volts.sort()
    volts.append(volts[len(volts) - 1] + 3)
    f.close()
    return


def plugEm():
    oneJoltCount = 0
    threeJoltCount = 0
    for i in range(len(volts) - 1):
        if(not volts[i + 1] - volts[i] < 4):
            #print(int(volts[i + 1]), int(volts[i]))
            return "error"
        elif(volts[i + 1] - volts[i] == 1):
            oneJoltCount += 1
        elif(volts[i + 1] - volts[i] == 3):
            threeJoltCount += 1
    print(oneJoltCount, threeJoltCount)
    return oneJoltCount * threeJoltCount


getVolts("input.txt")
print(plugEm())
