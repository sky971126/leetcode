#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
class Solution:

    def wordBreak(self, s, wordDict):
        good_index = set([-1])
        W = set(wordDict)
        for i in range(len(s)):
            for j in good_index:
                if s[j+1:i+1] in W:
                    good_index.add(i)
                    break
        return (len(s) - 1) in good_index

        