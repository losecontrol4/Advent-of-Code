def read_integers(filename):
    f = open(filename, 'r')
    list = []
    for line in f.readlines():
        list.append(int(line))
    f.close()
    return list


def answer():
    list = read_integers("input.txt")
    for i in range(len(list) - 1):
        for j in range(len(list)):
            if((list[i] + list[j]) == 2020):
                return list[i] * list[j]


print(answer())
