#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:

    #stupid n^2 try to find a step up
    """
    def trap(self, height):
        if not height:
            return 0
        water = [0]
        n = len(height)
        peak_all = 0
        for i in range(1, n):
            water.append(0)
            prev_peak_all = peak_all
            if height[peak_all] < height[i]:
                peak_all = i
            if height[i] > height[i-1]:
                peak_1 = i-1
                peak_2 = i
                seek_peak_1 = True
                seek_peak_2 = True
                for j in range(i-2,-1,-1):
                    if seek_peak_1:
                        peak_1 = j
                    peak_2 = j
                    #if (peak_1 < peak_all):
                        #peak_1 = i-1
                        #break
                    if (height[peak_1] > height[i-1]) and seek_peak_1:
                        seek_peak_1 = False
                    if (height[peak_2] > height[i]):
                        seek_peak_2 = False
                        break

                if not seek_peak_1: #peak 1 found, peak_1 to i
                    if height[i] <= height[peak_1]:
                        for j in range(peak_1+1, i):
                            water[j] = height[i]
                    elif not seek_peak_2: #peak 2 found, peak_2 to i
                        for j in range(peak_2+1,i):
                            water[j] = height[i]
                    else: #peak 2 not found, prev_peak_all to i
                        for j in range(prev_peak_all+1,i):
                            water[j] = height[prev_peak_all]
        sum = 0
        for i in range(1,n):
            value = water[i] - height[i]
            if value > 0:
                sum += value
        return sum
    """
    def trap(self, height):
        l = 0
        r = len(height) - 1
        area = 0
        max_l = 0
        max_r = 0
        while l <= r:
            if max_l <= max_r:
                if max_l > height[l]:
                    area += max_l - height[l]
                else:
                    max_l = height[l]
                l += 1
            else:
                if max_r > height[r]:
                    area += max_r - height[r]
                else:
                    max_r = height[r]
                r -= 1
        return area
#s = Solution()
#print(s.trap([2,0,2]))

