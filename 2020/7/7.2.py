

bagParent = []
bagContents = []


def setRules(fileName):
    f = open(fileName, 'r')
    rules = f.readlines()
    f.close()
    for rule in rules:
        # needed to keep the s for parents
        bagParent.append(rule.split(" contain ")[0])
        bagContents.append(rule.split("s contain ")[1])


def getBagIndex(bag):  # reversed it
    for x in range(len(bagParent)):
        # print(bagParent[x])
        if(bagParent[x].count(bag) != 0):
            return x
    # print(bag)


"""
for bag in pc:  # removes numbers and adds them to bagCount
        count = 0
        while(bag[count].isdigit()):
            count += 1
        bagCount += int(bag[:count])
        newPC.append(bag[count + 1:])
        """


def recursiveBagSearch(pc):  # changed to go the other way
    bagCount = 0
    if(len(pc) == 0):  # base case
        return 0
    else:
        for bag in pc:
            count = 0
            while(bag[count].isdigit()):
                count += 1
            result = recursiveBagSearch(
                getContentBags(bagContents[getBagIndex(bag[count + 1:])]))
            if result == 0:
                bagCount = bagCount + int(bag[:count])
            else:
                bagCount = bagCount + \
                    int(bag[:count]) + int(bag[:count]) * result
            print(bagCount, bag)
    return bagCount


# 2 shiny brown bags, 2 dull tan bags, 3 wavy coral bags, 2 pale lime bags.

###


def getContentBags(content):  # returns bags in content
    if(content.count("no other bags") > 0):
        return []
    return content[:(len(content) - 2)].split(", ")  # parsedContent


def answer(fileName, bagName):
    setRules(fileName)
    return recursiveBagSearch(getContentBags(bagContents[getBagIndex(bagName)]))


print(answer("input.txt", "shiny gold"))
