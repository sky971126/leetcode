#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        mono = []
        res = [0] * len(T)
        for i in range(len(T)):
            if mono and T[i] > T[mono[-1]]:
                while(mono and T[i] > T[mono[-1]]):
                    index = mono.pop()
                    res[index] = i - index
            mono.append(i)
        return res
# @lc code=end

