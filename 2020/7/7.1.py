

bagParent = []
bagContents = []
checkedBags = set()


def setRules(fileName):
    f = open(fileName, 'r')
    rules = f.readlines()
    f.close()
    for rule in rules:
        bagParent.append(rule.split("s contain ")[0])
        bagContents.append(rule.split("s contain ")[1])


def getBagIndex(bag):
    indexList = []
    for x in range(len(bagContents)):
        if(bagContents[x].count(bag) != 0):
            indexList.append(x)
    return indexList


def recursiveBagSearch(indexList):
    if(len(indexList) == 0):  # base case
        return
    else:
        for i in indexList:
            checkedBags.add(bagParent[i])
            recursiveBagSearch(getBagIndex(bagParent[i]))


def answer(fileName, bagName):
    setRules(fileName)
    recursiveBagSearch(getBagIndex(bagName))
    return len(checkedBags)


print(answer("input.txt", "shiny gold"))
