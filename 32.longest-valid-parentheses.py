#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    """
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        DP = [0] * len(s)
        if s[0] == "(" and s[1] == ")":
            DP[1] = 2
        for i in range(2,len(s)):
            if s[i] == "(":
                continue
            if s[i-1] == "(":
                DP[i] = DP[i-2] + 2
            else:
                if i-1-DP[i-1] > -1 and s[i-1-DP[i-1]] == "(":
                    DP[i] = DP[i-1] + 2
                    if i-1-DP[i-1]-1 > -1:
                        DP[i] += DP[i-1-DP[i-1]-1]
        return max(DP)
    """ 
    # No extra space
    def longestValidParentheses(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        for i in s:
            if i == "(":
                l += 1
            else:
                r += 1
            if l == r:
                max_len = max(max_len, 2 * l)
            elif l < r:
                l, r = 0, 0
        l, r = 0, 0
        for i in s[::-1]:
            if i == "(":
                l += 1
            else:
                r += 1
            if l == r:
                max_len = max(max_len, 2 * l)
            elif l > r:
                l, r = 0, 0
        return max_len




# @lc code=end