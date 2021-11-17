volts = []
answeredPaths = []


def getAnswerForPath(path):
    for i in range(len(answeredPaths)):
        if (answeredPaths[i][0] == path):
            return answeredPaths[i][1]
    return -1


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


def lookUp(index, num):
    look = getAnswerForPath((str(index) + " " + str(num)))
    if(look == -1):
        answer = plugEm(index, num)
        answeredPaths.append([str(index) + " " + str(num), answer])
        return answer
    else:
        return look


def plugEm(index, num):
    # base case
    try:
        if(volts[index + num] - volts[index] >= 4):
            return 0
        elif(volts[index + num] == volts[-1]):
            return 1
    except:
        return 0
    # lookUp is for efficency, honestly impressed they made a problem that my computer needed effciency things to be able to run in a reasonable time, the dag dynamic programming strat had such a large impact
    # this section allows me to store all the paths I already know.
    return lookUp(index + num, 1) + lookUp(index + num, 2) + lookUp(index + num, 3)


def plugEmAll():
    return plugEm(0, 1) + plugEm(0, 2) + plugEm(0, 3)


getVolts("input.txt")
print(plugEmAll())
