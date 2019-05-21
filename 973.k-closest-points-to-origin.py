#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = []
        for point in points:
            x, y = point
            dist.append([tuple(point), x * x + y * y])
        dist.sort(key=lambda p: p[1])
        return [i[0] for i in dist[:K]]
