#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        def findSubsequences(nums):
            if not nums:
                return []
            res = []
            res.append((nums[0],))
            for num in nums[1:]:
                for seq in res:
                    if seq[-1] < num:
                        res.append(seq + (num,))
                res.append((num,))
            return res
        
        res = findSubsequences(nums)
        max_len = 0
        count = 0
        for i in res:
            if max_len < len(i):
                max_len = len(i)
                count = 1
            elif max_len == len(i):
                count += 1
        return count
             
# @lc code=end

