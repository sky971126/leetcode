#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        trig = 0
        nontrig = 0
        for num in nums:
            tmp = trig
            trig = nontrig + num
            nontrig = max(tmp, nontrig)
        return max(trig, nontrig)

# @lc code=end

