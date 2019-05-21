#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        if k == 1:
            return nums
        deq = deque()
        max_index = 0
        max_num = nums[0]
        def clean(i):
            if deq and deq[0] == i-k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        for i in range(k):
            clean(i)
            deq.append(i)
            if max_num <= nums[i]:
                max_num = nums[i]
                max_index = i
        results = [nums[max_index]]
        for i in range(k, n):
            clean(i)
            deq.append(i)
            results.append(nums[deq[0]])
        return results
