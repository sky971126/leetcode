#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(0,len(A)-1):
            if A[i] > A[i+1]:
                return i
        return len(A) - 1

# @lc code=end

