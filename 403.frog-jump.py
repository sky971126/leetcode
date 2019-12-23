#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        D = {}
        for stone in stones:
            D[stone] = set()
        D[0].add(1)
        for stone in stones[:-1]:
            for step in D[stone]:
                if stone + step in D:
                    if step > 0:
                        D[stone + step].add(step-1)
                        D[stone + step].add(step)
                        D[stone + step].add(step+1)
        if D[stones[-1]]:
            return True
        else:
            return False
# @lc code=end

