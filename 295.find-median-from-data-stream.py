#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
import heapq as hq
class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h1 = [] #max heap with negative nums
        self.h2 = [] #min heap

    def addNum(self, num: int) -> None:
        h1 = self.h1
        h2 = self.h2
        if not h2:
            hq.heappush(h2, num)
            return
        if h2[0] > num:
            if len(h1) < len(h2):
                hq.heappush(h1, -num)
            else:
                if -h1[0] > num:
                    max_h1 = -hq.heappop(h1)
                    hq.heappush(h1, -num)
                    hq.heappush(h2, max_h1)
                else:
                    hq.heappush(h2, num)
        else:
            if len(h1) < len(h2):
                if h2[0] < num: 
                    min_h2 = hq.heappop(h2)
                    hq.heappush(h2, num)
                    hq.heappush(h1, -min_h2)
                else:
                    hq.heappush(h1, -num)
            else:
                hq.heappush(h2, num)

    def findMedian(self) -> float:
        h1 = self.h1
        h2 = self.h2
        if len(h1) == len(h2):
            return (h2[0] - h1[0]) / 2
        else:
            return h2[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

