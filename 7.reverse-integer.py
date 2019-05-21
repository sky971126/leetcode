#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x):
        sign = x >= 0
        x = abs(x)
        rev = 0
        while x > 0:
            remain = x % 10
            x = (x - remain) // 10
            rev = rev * 10 + remain
        if rev > pow(2, 31) - 1:
            return 0
        if not sign:
            rev = -rev
        return rev

#print(Solution().reverse(123))
