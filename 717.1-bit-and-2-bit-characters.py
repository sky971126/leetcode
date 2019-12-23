#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        one = True
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                one = False
            else:
                i += 1
                one = True
        return one

# @lc code=end

