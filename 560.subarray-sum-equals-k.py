#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        result = 0
        if nums[0] == k:
            result += 1
        for i in range(1,n):
            nums[i] += nums[i-1]
            if nums[i] == k:
                result += 1
        for i in range(n-1):
            for j in range(i+1,n):
                nums[j] = nums[j] - nums[i]
                if nums[j] == k:
                    result += 1
        return result

#Solution().subarraySum([1,2,3,4],10)