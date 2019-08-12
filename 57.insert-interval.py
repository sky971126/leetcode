#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        sta, end = newInterval
        before = []
        middle = []
        i = 0
        for i in range(len(intervals)):
            sta_i, end_i = intervals[i]
            if sta > end_i:
                before.append(intervals[i])
            else:
                middle.append(min(sta, sta_i))
                break
        if not middle:
            return intervals + [newInterval]

        j = i + 1
        for j in range(i+1, len(intervals)):
            sta_j, end_j = intervals[j]
            if end < sta_j:
                if end >= intervals[j-1][0]:
                    middle.append(max(end, intervals[j-1][1]))
                else:
                    middle.append(end)
                    j -= 1
                break
        if len(middle) == 1:
            if end >= intervals[-1][0]:
                middle.append(max(end, intervals[-1][1]))
                return before + [middle]
            else:
                middle.append(end)
                return before + [middle] + [intervals[-1]]
        return before + [middle] + intervals[j:]
#print(Solution().insert([[2,5],[6,7],[8,9]],[0,1]))
