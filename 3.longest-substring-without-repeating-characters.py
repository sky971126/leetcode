#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        if n == 0:
            return 0
        max_len = 1
        mov_len = 0
        rep = {}
        start = 0
        for i in range(n):
            if s[i] not in rep:
                mov_len += 1
                rep[s[i]] = i
            else:
                duplicate = rep[s[i]] + 1
                for j in range(start, duplicate):
                    rep.pop(s[j])
                start = duplicate
                if mov_len > max_len:
                    max_len = mov_len
                rep[s[i]] = i
                mov_len = i - start + 1
        return max(max_len, mov_len)

#print(Solution().lengthOfLongestSubstring("dvdf"))