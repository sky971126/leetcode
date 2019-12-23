def solution(tasks, weights, p):
    n = len(tasks)
    tasks = [i * 2 for i in tasks]
    DP = [[0] * n for _ in range(p+1)]
    for j in range(n):
        DP[0][j] = 0
    for i in range(p+1):
        if i >= tasks[0]:
            DP[i][0] = weights[0]
    for i in range(1, p+1):
        for j in range(1, n):
            DP[i][j] = DP[i][j-1]
            if i >= tasks[j]:
                DP[i][j] = max(DP[i][j], DP[i-tasks[j]][j-1]+weights[j])
    print(DP)
    return DP[p][n-1]

print(solution([3,3,2,2],[3,3,2,2],9))