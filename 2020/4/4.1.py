

def getPassports(fileName):
    f = open(fileName, 'r')
    passports = f.read().split("\n\n")
    f.close()
    return passports


def hasCID(passport):
    return passport.count("cid") > 0


def isValidPassport(passport):
    items = passport.split()
    if(len(items) < 7):
        return False
    elif len(items) == 8:
        return True
    else:
        return not hasCID(passport)


passports = getPassports("input.txt")
validCount = 0
for passport in passports:
    if isValidPassport(passport):
        validCount += 1
print(validCount)
