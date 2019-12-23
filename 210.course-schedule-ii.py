#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        c2p = collections.defaultdict(set)
        p2c = collections.defaultdict(list)
        basic = set(range(numCourses))
        for course, pre in prerequisites:
            p2c[pre].append(course)
            c2p[course].add(pre)
            if course in basic:
                basic.remove(course)
        order = []
        while len(basic):
            b = basic.pop()
            order.append(b)
            for c in p2c[b]:
                c2p[c].remove(b)
                if not c2p[c]:
                    basic.add(c)
            p2c.pop(b)
        if len(order) == numCourses:
            return order
        else:
            return []
# @lc code=end

