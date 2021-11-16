

import string


def getPassports(fileName):
    f = open(fileName, 'r')
    passports = f.read().split("\n\n")
    f.close()
    return passports


def hasCID(passport):
    return passport.count("cid") > 0


def validKeyValue(key, value):  # byr iyr eyr hgt hcl ecl pid cid
   # print(value)
    if key == "byr":
        value = int(value)
        return (value >= 1920 and value <= 2002)
    elif key == "iyr":
        value = int(value)
        return (value >= 2010 and value <= 2020)
    elif key == "eyr":
        value = int(value)
        return (value >= 2020 and value <= 2030)
    elif key == "hgt":
        unit = value[-2:]
        if not unit.isalpha():
            return False
        value = int(value[:-2])
        if unit == "cm":
            return (value >= 150 and value <= 193)
        elif unit == "in":
            return (value >= 59 and value <= 76)
        else:
            return False
    elif key == "hcl":
        if value[0] == '#':
            for i in range(1, 6):
                if(string.ascii_lowercase[:6].find(value[i]) == -1 and not value[i].isalnum):
                    return False
            return True  # If every char passes the test it is valid
        else:
            return False
    elif key == "ecl":
        if(len(value) != 3):
            return False
        return (value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth")

    elif key == "pid":
        return (len(value) == 9 and value.isalnum)
    elif key == "cid":
        return True
    else:
        return False


def isValidPassport(passport):
    items = passport.split()
    if((len(items) < 7) or ((len(items) < 8 and hasCID(passport)))):
        return False
    for item in items:
        key = item.split(':')[0]
        value = item.split(':')[1]
        if not validKeyValue(key, value):
            return False
    return True


passports = getPassports("input.txt")
validCount = 0
for passport in passports:
    if isValidPassport(passport):
        validCount += 1
print(validCount)
