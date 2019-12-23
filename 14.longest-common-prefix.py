#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        prefix = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return prefix
            prefix += c
        return prefix
# @lc code=end

Solution().longestCommonPrefix(["flower","flow","flight"])
