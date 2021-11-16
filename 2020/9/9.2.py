nums = []
PSIZE = 25  # 5 for inputT.txt


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


def findCSet(weakness):
    for i in range(len(nums)):
        sum = 0
        count = 0 + i
        c_set = []
        while(sum < weakness):
            sum += int(nums[count])
            c_set.append(int(nums[count]))
            count += 1
        if sum == weakness:
            return min(c_set) + max(c_set)


getNums("input.txt")
weakness = findFirstError()
print(findCSet(weakness))
