#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
import collections
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        if k == 0:
            for _, value in collections.Counter(nums).items():
                if value >= 2:
                    res += 1
            return res
        if k < 0:
            return 0
        unique = set(nums)
        for i in unique:
            if i + k in unique:
                res += 1
        return res
# @lc code=end

