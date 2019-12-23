#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
import math
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)*2 - 1):
            l = i >> 1
            r = math.ceil(i/2)
            while(l>-1 and r<len(s) and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
        return res
# @lc code=end

