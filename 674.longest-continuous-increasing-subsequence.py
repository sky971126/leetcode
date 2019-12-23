#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        temp = 0
        for i in range(len(nums)-1):
            temp += 1
            if nums[i] >= nums[i+1]:
                res = max(res, temp)
                temp = 0
        return max(res, temp+1)
                
# @lc code=end

