f = open("input.txt", 'r')
nums = f.readlines()
f.close()
count = 0
for i in range(1, len(nums)):
    if(int(nums[i]) > int(nums[i-1])):
        count += 1
print(count)
