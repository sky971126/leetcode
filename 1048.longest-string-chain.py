#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
import collections
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        DP = collections.defaultdict(int)
        words.sort(key = lambda x: len(x))
        for word in words:
            longest = 1
            for i in range(len(word)):
                trim = word[:i] + word[i+1:]
                longest = max(longest, DP[trim]+1)
            DP[word] = longest
        return max(DP.values())
    
# @lc code=end

