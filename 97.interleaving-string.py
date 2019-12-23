#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        def isInterleave_helper(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if dp[i][j]:
                return False
            if i < len(s1) and s1[i] == s3[i+j]:
                if isInterleave_helper(i+1, j):
                    return True
            if j < len(s2) and s2[j] == s3[i+j]:
                if isInterleave_helper(i, j+1):
                    return True
            dp[i][j] = 1
            return False
        
        return isInterleave_helper(0, 0)


# @lc code=end

