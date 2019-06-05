#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        if m > n:
            m, n = n, m
        result = 1
        for i in range(m):
            result = result * (n + i + 1) / (i + 1)
        return int(result)

