#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
import collections
class Solution:
    def criticalConnections(self, n: int, connections):
        index = {}
        low = {}
        G = collections.defaultdict(list)
        for v1, v2 in connections:
            G[v1].append(v2)
            G[v2].append(v1)
        i = 0
        res = []
        def dfs(v, parent):
            nonlocal i
            index[v] = i
            low[v] = i
            i += 1
            for u in G[v]:
                if u == parent:
                    continue
                if u not in index:
                    dfs(u, v)
                low[v] = min(low[v], low[u])
            if parent != None and low[v] == index[v]:
                res.append([parent, v])
        dfs(0, None)
        return res


# @lc code=end
print(Solution().criticalConnections(5, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]))

print(Solution().criticalConnections(5, [[0,1], [0, 2], [1, 2], [0, 3], [3, 4]]))
print(Solution().criticalConnections(4, [[0,1], [1, 2], [2, 3]]))
print(Solution().criticalConnections(5, [[0,1], [1, 2], [2, 0], [1, 3], [1, 4], [1, 6], [3, 5], [4, 5]]))
