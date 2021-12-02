f = open("input.txt", 'r')
data = f.readlines()
hp = 0
depth = 0
aim = 0
for i in range(len(data)):
    d = data[i].split()[0]
    num = data[i].split()[1]
    if(d == "down"):
        aim += int(num)
    if(d == "up"):
        aim -= int(num)
    if(d == "forward"):
        hp += int(num)
        depth += aim * int(num)
print(depth * hp)
