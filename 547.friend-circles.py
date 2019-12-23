#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution:
    def findCircleNum(self, M) -> int:
        n = len(M)
        roots = list(range(n))
        ranks = [0] * n
        
        def find(i):
            while i != roots[i]:
                i = roots[i]
            return i

        def union(i,j):
            ri = find(i)
            rj = find(j)
            if ri == rj:
                return
            elif ranks[ri] < ranks[rj]:
                roots[ri] = rj
            else:
                roots[rj] = ri
                if ranks[ri] == ranks[rj]:
                    ranks[ri] += 1
        
        for i in range(1, n):
            for j in range(i):
                if M[i][j]:
                    union(i,j)

        return len(set([find(i) for i in roots]))

#print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
# @lc code=end

