def solution(A, k):
    l = 1
    r = max(A)
    res = 0
    while (l <= r):
        m = (l+r) // 2
        k_cur = 0
        for i in A:
            k_cur += i // m
        if k_cur >= k:
            res = max(res, m)
            l = m + 1
        else:
            r = m - 1
    return res
print(solution([1,2,3,4,9],20))