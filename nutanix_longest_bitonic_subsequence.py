def solution(nums):
    n = len(nums)
    d1 = [1] * n
    d2 = [1] * n
    def longest(nums, d):
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    d[i] = max(d[i], d[j] + 1)
    longest(nums, d1)
    longest(nums[::-1], d2)
    print(d1)
    print(d2)
    res = 0
    for i in range(n):
        res = max(res, d1[i] + d2[n-1-i])
    return res - 1

print(solution([80, 60, 30, 40, 20, 10]))