#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        split = nums[-1]
        n = len(nums)
        if target == split:
            return n-1
        else:
            target_in_first = target > split
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            else:
                if nums[m] > split: # m in first part
                    if target_in_first:
                        if nums[m] > target:
                            r = m - 1
                        else:
                            l = m + 1
                    else:
                        l = m + 1
                else: # m in second part
                    if target_in_first:
                        r = m - 1
                    else:
                        if nums[m] > target:
                            r = m - 1
                        else:
                            l = m + 1
        return -1

            

