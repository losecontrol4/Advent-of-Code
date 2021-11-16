f = open("input.txt", 'r')
map = f.readlines()
f.close()


def getTreeCount(right, down):
    treeCount = 0
    lineLength = len(map[0]) - 1
    for i in range(0, len(map) - 1, down):
        x = (int(i/down) * right + right) % lineLength
        y = i + down
        if(map[y][x] == '#'):
            treeCount += 1
    return treeCount


a = getTreeCount
answer = a(1, 1) * a(3, 1) * a(5, 1) * a(7, 1) * a(1, 2)
print(answer)
print(a(1, 1))
print(a(3, 1))
print(a(5, 1))
print(a(7, 1))
print(a(1, 2))
