import string

ALP = string.ascii_lowercase
print(ALP)


def getGroups(fileName):
    f = open(fileName, 'r')
    groups = f.read().split("\n\n")
    f.close()
    return groups


def getYesCount(group):
    yesCount = 0
    for char in ALP:
        # I would use something other than .count() if I were to try to make this more efficient. I only need to know there one in there, not how many.
        if(group.count(char) > 0):
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
