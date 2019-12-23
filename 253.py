class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort(key=lambda x: x[0])
        mono = []
        res = 0
        for interval in intervals:
            l, r = interval
            while mono and mono[-1] <= l:
                mono.pop()
            i = 0
            for i in range(len(mono)):
                if mono[i] < r:
                    break
            if i == len(mono) - 1 and mono[i] > r:
                mono.append(r)
            else:
                mono.insert(i, r)
            res = max(res, len(mono))
            print(mono)
        return res

Solution().minMeetingRooms([[9,10],[4,9],[4,17]])