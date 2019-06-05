#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
class Solution:
    def leastInterval(self, tasks, n):
        task_map = [0] * 26
        for t in tasks:
            task_map[ord(t) - 65] += 1
        task_map.sort(reverse = True)
        result = 0
        while task_map[0] > 0:
            time = 0
            for i in range(0, n+1):
                if task_map[i] == 0:
                    break
                task_map[i] -= 1
                time += 1
            task_map.sort(reverse = True)
            if task_map[0] > 0:
                result += n + 1
            else:
                result += time
        return result

#print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
