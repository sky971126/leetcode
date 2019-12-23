#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        sat = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                sat += customers[i]
            customers[i] *= grumpy[i]
        res = temp = sum(customers[:X])
        for i in range(1, len(customers) - X + 1):
            temp = temp - customers[i-1] + customers[X-1+i]
            res = max(res, temp)
        return res + sat
# @lc code=end

