import string

ALP = string.ascii_lowercase


def getGroups(fileName):
    f = open(fileName, 'r')
    groups = f.read().split("\n\n")
    f.close()
    return groups


def getYesCount(group):
    yesCount = 0
    gmc = len(group.split("\n"))  # group member count
    for char in ALP:
        if(group.count(char) == gmc):
            yesCount += 1
    return yesCount


def getYesSum(groups):
    sum = 0
    for group in groups:
        sum = sum + getYesCount(group)
    return sum
    # print(getGroups("input.txt"))
    # print(getYesCount("aaaaab\nas"))


print(getYesSum(getGroups("input.txt")))
