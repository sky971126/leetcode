#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        good_index = set([-1])
        W = set(wordDict)
        for i in range(len(s)):
            for j in good_index:
                if s[j+1:i+1] in W:
                    good_index.add(i)
                    break
        return (len(s) - 1) in good_index
            
# @lc code=end

