def solution(A, p, s, t):

    DP = {}
    n = len(A)
    DP[n-1] = 1
    DP[n] = 0

    def solution_helper(index):
        nonlocal p, s, t
        if index in DP:
            return DP[index]
        elif A[index] != A[index+1]:
            DP[index] = max(solution_helper(index+2) + p, solution_helper(index+1) + s)
            return DP[index]
        else:
            DP[index] = max(solution_helper(index+2) + p - t, solution_helper(index+1) + s)
            return DP[index]
    
    return solution_helper(0)

print(solution("110", 4, 2, 1))
print(solution("11", 4, 2, 1))
print(solution("101", 4, 1, 1))