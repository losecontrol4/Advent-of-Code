f = open("input.txt", 'r')
map = f.readlines()
f.close()
treeCount = 0
lineLength = len(map[0]) - 1
for i in range(len(map) - 1):
    x = (i * 3 + 3) % lineLength
    y = i + 1
    if(map[y][x] == '#'):
        treeCount += 1
        map[y] = map[y][:x] + 'X' + map[y][(x+1):]
    else:
        map[y] = map[y][:x] + '0' + map[y][(x+1):]
f = open('output.txt', 'w')
f.writelines(map)
f.close
print(treeCount)
