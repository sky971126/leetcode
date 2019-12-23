#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        if n < 2:
            return True
        min_good = n-1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= min_good:
                min_good = i
        return min_good == 0

# @lc code=end

