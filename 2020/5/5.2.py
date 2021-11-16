import math

MAXROW = 127
MAXCOL = 7


def getTickets(fileName):
    f = open(fileName, 'r')
    tickets = f.readlines()
    return tickets


def getSeatID(ticket):
    row = MAXROW + 1
    rowMin = 0 + 1
    col = MAXCOL + 1
    colMin = 0 + 1
    count = 0
    while(ticket[count] == 'F' or ticket[count] == 'B'):
        if ticket[count] == 'B':
            rowMin = row//2 + math.ceil(rowMin/2)
        else:
            row = row // 2 + rowMin//2
        count += 1
    while(count < len(ticket)):
        if ticket[count] == 'R':
            colMin = col//2 + math.ceil(colMin/2)
        elif ticket[count] == 'L':
            col = col // 2 + colMin//2
        count += 1

    #print(row - 1, col - 1, (row - 1) * 8 + (col - 1))
    return((row - 1) * 8 + (col - 1))


def answer(fileName):
    tickets = getTickets(fileName)
    seatIDs = []
    for ticket in tickets:
        seatIDs.append(getSeatID(ticket))
    seatIDs.sort()
    for x in range(len(seatIDs)):
        if(x + seatIDs[0] != seatIDs[x]):
            return x + seatIDs[0]


print(answer("input.txt"))
