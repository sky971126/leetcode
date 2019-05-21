#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_complement = {}
        for i in range(len(nums)):
            if (nums[i] in target_complement):
                return [target_complement[nums[i]], i]
            target_complement[target - nums[i]] = i

