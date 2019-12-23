def readIn():
    n = int(input())
    A = []
    for i in range(n):
        whole = []
        for _ in range(3):
            line = [int(i) for i in input().split(" ")]
            whole.append(line)
        A.append(whole)
        if i != n-1:
            input()
    return A
A = readIn()

def checkNum(b):
    x, o = 0, 0
    for i in range(3):
        for j in range(3):
            if b[i][j] == 1:
                x += 1
            elif b[i][j] == 2:
                o += 1
    return x, o

def same(a,b,c,d):
    if a == b and a == c and a == d:
        return True
    return False

def checkWin(b, which):
    win = 0
    for i in range(3):
        if same(b[i][0], b[i][1], b[i][2], which):
            win += 1
    for i in range(3):
        if same(b[0][i], b[1][i], b[2][i], which):
            win += 1
    if same(b[0][0], b[1][1], b[2][2], which):
        win += 1
    if same(b[0][2], b[1][1], b[2][0], which):
        win += 1
    return win

def checkWinAfterMove(b, which):
    win = 0
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0:
                bcopy = b.copy()
                bcopy[i][j] = which
                if checkWin(bcopy, which):
                    win += 1
    return win

def checkDoubleProbAfterMove(b, which):
    for i in range(3):
        for j in range(3):
            if b[i][j] == 0:
                bcopy = b.copy()
                bcopy[i][j] = which
                if checkWinAfterMove(bcopy, which) > 1:
                    return True
    return False


#print(checkNum(A[0]))
#print(checkWin(A[2], 1))

for b in A:
    x, o = checkNum(b)
    next_move = None
    oppo = None
    if x == o:
        next_move = 1
        oppo = 2
    elif x == o + 1:
        next_move = 2
        oppo = 1
    else:
        print(-1)
        continue

    x_win = checkWin(b, 1)
    o_win = checkWin(b, 2)
    if x_win and o_win:
        print(-1)
        continue
    elif x_win:
        print(1)
        continue
    elif o_win:
        print(2)
        continue
    
    next_win = checkWinAfterMove(b, next_move)
    if next_win:
        print(next_move)
        continue
    oppo_win = checkWinAfterMove(b, oppo)
    if oppo_win > 1:
        print(oppo)
        continue

    next_next_win = checkDoubleProbAfterMove(b, next_move)
    if next_next_win:
        print(next_move)
        continue

    print(0)