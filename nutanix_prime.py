def solution(n):
    m = (n - 2) // 2 
    A = [0] * (m + 1)
    for i in range(1, m):
        j = i
        while (i+j+2*i*j <= m):
            A[i+j+2*i*j] = 1
            j += 1
    res = [2]
    for i in range(1,m+1):
        if A[i] == 0:
            res.append(2*i+1)
    print(res)
    return res

solution(100)
