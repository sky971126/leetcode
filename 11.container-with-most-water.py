#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    
    # stupid time limit exceeded
    """
    def maxArea(self, height):
        n = len(height)
        l = [[height[i], i] for i in range(n)]
        l = sorted(l, reverse=True)
        max = 0
        for i in range(n):
            min_leng = 0
            for j in range(i+1,n):
                leng = abs(l[j][1] - l[i][1])
                if leng > min_leng:
                    min_leng = leng
                    area = l[j][0] * leng
                    if area > max:
                        max = area
        return max
    """
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0
        while l<r:
            max_area = max(max_area, min(height[l],height[r]) * (r-l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1 
        return max_area

#s = Solution()
#print(s.maxArea([1,2,4,3]))

