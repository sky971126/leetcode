#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        DP = {}
        def combinationSum4_helper(target):
            if target in DP:
                return DP[target]
            if target == 0:
                return 1
            if target < 0:
                return 0
            s = 0
            for i in nums:
                s += combinationSum4_helper(target-i)
            DP[target] = s 
            return s
        return combinationSum4_helper(target)
# @lc code=end

