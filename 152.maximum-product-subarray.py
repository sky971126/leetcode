#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
class Solution:
    def maxProduct(self, nums):
        max_i = nums[0]
        min_i = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_i, min_i = min_i, max_i
            max_i = max(nums[i], max_i * nums[i])
            min_i = min(nums[i], min_i * nums[i])
            res = max(res, max_i)
        return res

    
