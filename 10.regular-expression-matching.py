#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def isMatch_helper(i, j):
            if (i,j) in dp:
                return dp[i,j]
            if j == len(p):
                dp[i,j] = (i == len(s))
            else:
                first_match = i < len(s) and (p[j] in [s[i], '.'])
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i,j] = isMatch_helper(i,j+2) or (first_match and isMatch_helper(i+1, j))
                else:
                    dp[i,j] = first_match and isMatch_helper(i+1, j+1)
            return dp[i,j]
        return isMatch_helper(0, 0)
        

