#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums):
        results = []
        self.permute_helper(nums, [], results)
        return results

    def permute_helper(self, nums, result, results):
        if not nums:
            results.append(result)
            return
        for i in range(len(nums)):
            self.permute_helper(nums[:i]+nums[i+1:], result+[nums[i]], results)
