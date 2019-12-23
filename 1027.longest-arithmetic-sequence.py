#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Sequence
#

# @lc code=start
import collections
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(1, len(A)):
            for j in range(i):
                dp[A[i] - A[j],i] = dp.get((A[i] - A[j], j), 1) + 1
        return max(dp.values())

# @lc code=end

