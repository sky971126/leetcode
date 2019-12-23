#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        c2p = collections.defaultdict(set)
        p2c = collections.defaultdict(list)
        basic = set(range(numCourses))
        for course, pre in prerequisites:
            p2c[pre].append(course)
            c2p[course].add(pre)
            if course in basic:
                basic.remove(course)
        # print(c2p)
        # print(p2c)
        # print(basic)
        while len(basic):
            b = basic.pop()
            for c in p2c[b]:
                c2p[c].remove(b)
                if not c2p[c]:
                    basic.add(c)
            p2c.pop(b)
        if p2c:
            return False
        else:
            return True

# @lc code=end

Solution().canFinish(3,[[2,0],[2,1]])
