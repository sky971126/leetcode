#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
class Solution:
    def combine(self, n, k):
        res_list = []
        self.combine_helper(res_list, [], list(range(1,n+1)), k)
        return res_list

    def combine_helper(self, res_list, res, nums, k):
        if len(res) == k:
            res_list.append(res)
        if not nums:
            return
        for i in range(len(nums)):
            num = nums[i]
            self.combine_helper(res_list, res+[num], nums[i+1:], k)
