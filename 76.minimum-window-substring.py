#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        min_size = float("inf")
        ct = {}
        ct_t = collections.Counter(t)
        for c in t:
            ct[c] = 0
        start = 0
        formed = 0

        for r in range(len(s)):
            if s[r] in ct:
                ct[s[r]] += 1
                if ct[s[r]] == ct_t[s[r]]:
                    formed += 1
            if formed < len(ct):
                continue
            l = start
            for l in range(start, r+1):
                if s[l] in ct:
                    ct[s[l]] -= 1
                    if ct[s[l]] < ct_t[s[l]]:
                        formed -= 1
                        break
            size = r - l + 1
            start = l + 1
            if size < min_size:
                min_size = size
                res = s[l:r+1]
        return res
# @lc code=end

