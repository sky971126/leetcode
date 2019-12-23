#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0
        points.sort(key = lambda x: x[0])
        cut = 1
        x0, y0 = points[0]
        for i in range(1, len(points)):
            x1, y1 = points[i]
            if x1 <= y0:
                x0 = x1
                y0 = min(y0, y1)
            else:
                cut += 1
                x0, y0 = points[i]
        return cut


# @lc code=end

Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])