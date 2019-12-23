#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        diff2index = {0:-1}
        diff = 0
        max_len = 0
        for i, num in enumerate(nums):
            if num == 1:
                diff += 1
            else:
                diff -= 1
            if diff in diff2index:
                max_len = max(max_len, i - diff2index[diff])
            else:
                diff2index[diff] = i
        return max_len

# @lc code=end

