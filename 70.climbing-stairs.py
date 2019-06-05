#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    import math
    def climbStairs(self, n: int) -> int:
        """
        n_1 = 1
        n_2 = 2
        for i in range(0, n)
        """
        sqrt5 = math.sqrt(5)
        return int((((1+sqrt5)/2) ** (n+1) - ((1-sqrt5)/2) ** (n+1)) / sqrt5)
        
        

