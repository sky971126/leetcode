def solution(A):
    res = 0
    for i in range(len(A)-2):
        a, b, c = A[i], A[i+1], A[i+2]
        if a!=b and a!=c and b!=c:
            res += 1
    return res

print(solution("aabdcreff"))