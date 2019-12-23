#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while (X < Y):
            if Y % 2 == 0:
                Y = Y // 2
            else:
                Y = Y + 1
            res += 1
        return res + X - Y
# @lc code=end

