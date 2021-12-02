f = open("input.txt", 'r')
data = f.readlines()
f.close()
hp = 0
depth = 0
for i in range(len(data)):
    d = data[i].split()[0]
    num = data[i].split()[1]
    if(d == "down"):
        depth += int(num)
    if(d == "up"):
        depth -= int(num)
    if(d == "forward"):
        hp += int(num)
print(depth * hp)
