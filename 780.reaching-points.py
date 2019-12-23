#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while (tx > 0 and ty > 0):
            if tx == sx:
                if (ty - sy) >= 0 and (ty - sy) % sx == 0:
                    return True
                else:
                    return False
            if ty == sy:
                if (tx -sx) >= 0 and (tx- sx) % ty == 0:
                    return True
                else:
                    return False
            if tx > ty:
                tx %= ty
            elif tx < ty:
                ty %= tx
            else:
                return False
        return False
# @lc code=end

