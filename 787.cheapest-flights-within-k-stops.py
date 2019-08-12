#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst:
            return 0
        PRICE = {}
        COST = {}
        for flight in flights:
            s, d, p = flight
            COST[s] = -1
            COST[d] = -1
            if s not in PRICE:
                PRICE[s] = {d:p}
            else:
                PRICE[s][d] = p
        src_list = [src]
        COST[src] = 0
        for k in range(K + 1):
            src_list_new = []
            COST_TMP = {}
            for s in src_list:
                if s == dst:
                    continue
                if s in PRICE:
                    for (d, p) in PRICE[s].items():
                        if COST[d] < 0:
                            if d in COST_TMP:
                                COST_TMP[d] = min(COST_TMP[d], COST[s] + p)
                            else:
                                COST_TMP[d] = COST[s] + p
                            src_list_new.append(d)
                        else:
                            if COST[d] > COST[s] + p:
                                if d in COST_TMP:
                                    COST_TMP[d] = min(COST_TMP[d], COST[s] + p)
                                else:
                                    COST_TMP[d] = COST_TMP[d] = COST[s] + p
                                src_list_new.append(d)
            src_list = src_list_new
            for (d, c) in COST_TMP.items():
                COST[d] = c
        return COST[dst]

#print(Solution().findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1))

