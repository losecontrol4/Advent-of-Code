f = open("input.txt", 'r')
nums = f.readlines()
f.close()
count = 0
window = 0
oldWindow = 0
firstPass = False
for i in range(2, len(nums)):
    window = int(nums[i]) + int(nums[i - 1]) + int(nums[i - 2])
    if(window > oldWindow and firstPass):
        count += 1
    oldWindow = window
    firstPass = True
print(count)
