#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        l = 0
        for num in s:
            if num-1 not in s:
                l_cur = 1
                num_cur = num
                while num_cur + 1 in s:
                    l_cur += 1
                    num_cur += 1
                l = max(l, l_cur)
        return l
