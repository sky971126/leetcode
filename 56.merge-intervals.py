#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    """
    def merge(self, intervals):
        n = len(intervals)
        results = []
        for interval in intervals:
            l, r = interval
            merged = False
            for merged_interval in results:
                ml, mr = merged_interval
                if l <= ml <= r or l <= mr <= r or ml <= l <= mr:
                    merged = True
                    l = min(l, ml)
                    r = max(r, mr)
                    merged_interval[0] = l
                    merged_interval[1] = r
            if not merged:
                results.append(interval)
            else:
                results = [i for i in results if not (l<=i[0] and i[1]<=r)]
                results.append([l,r])
        return results
    """
    
    #sort
    def merge(self, intervals):
        if intervals == []:
            return []
        intervals.sort()
        n = len(intervals)
        l, r = intervals[0]
        results = []
        for i in range(1,n):
            l_i, r_i = intervals[i]
            if r >= l_i:
                merged = True
                r = max(r_i, r)
            else:
                results.append([l, r])
                l = l_i
                r = r_i
        results.append([l, r])
        return results

#print(Solution().merge([[1,3],[4,7],[2,6]]))

