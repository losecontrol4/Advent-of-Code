nums = []
PSIZE = 25


def getNums(fileName):
    f = open(fileName, 'r')
    global nums
    nums = f.readlines()
    f.close()


def findFirstError():
    for num in range(PSIZE, len(nums)):
        if(not isValid(num)):
            return int(nums[num])


def isValid(num):
    for i in range(PSIZE - 1):
        for j in range(1, PSIZE):
            if (int(nums[num - (i + 1)]) + int(nums[num - (j + 1)]) == int(nums[num])) and (int(nums[num - (i + 1)]) != int(nums[num - (j + 1)])):
                #print(int(nums[num - (i + 1)]), int(nums[num - (j + 1)]), int(nums[num]))
                return True
    return False


getNums("input.txt")
print(findFirstError())
