#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def process(n):
            res = 0
            while n > 0:
                remainder = n % 10
                res += remainder ** 2
                n = n // 10
            return res
        s = set()
        while 1:
            n = process(n)
            if n == 1:
                return True
            if n in s:
                return False
            s.add(n)



# @lc code=end

Solution().isHappy(19)