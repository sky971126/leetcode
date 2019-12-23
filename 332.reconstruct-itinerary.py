#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
import collections

class Solution:
    def findItinerary(self, tickets):
        D = collections.defaultdict(list)
        for s, d in tickets:
            D[s].append(d)
        for value in D.values():
            value.sort(reverse=True)
        route=[]
        """ recursive
        def visit(cur):
            while (D[cur]):
                nex = D[cur].pop()
                visit(nex)
            route.append(cur)
        visit("JFK")
        """
        # iterative
        stack = ["JFK"]
        while stack:
            while D[stack[-1]]:
                stack.append(D[stack[-1]].pop())
            route.append(stack.pop())

        return route[::-1]
    
#print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# @lc code=end

