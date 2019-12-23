#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, A, B) -> int:
        n = len(A)
        m = len(B)
        dp = [0] * (m+1) # for dp  index+1
        res = 0
        for i in range(n):
            tmp = dp[0]
            for j in range(m):
                new_tmp = dp[j+1]
                if B[j] == A[i]:
                    dp[j+1] = tmp + 1
                    res = max(res, dp[j+1])
                else:
                    dp[j+1] = 0
                tmp = new_tmp
        return res
            

# @lc code=end
Solution().findLength([0,0,0,0,1],
[1,0,0,0,0])