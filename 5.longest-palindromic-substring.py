#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        longest = []
        n = len(s)
        for i in range(1, n-1):
            if s[i+1] == s[i-1]:
                longest.append([i-1,i+1])
        for i in range(0, n-1):
            if s[i] == s[i+1]:
                longest.append([i,i+1])
        if longest == []:
            return s[0]

        while(1):
            new_longest = []
            for pal in longest:
                if (pal[0] > 0) and (pal[1] < n-1) and (s[pal[0]-1] == s[pal[1]+1]):
                    pal[0] = pal[0] - 1
                    pal[1] = pal[1] + 1
                    new_longest.append(pal)
            if len(new_longest) == 0:
                break
            else:
                longest = new_longest

        max_pal = longest[0]
        for pal in longest:
            if (pal[1] - pal[0]) > (max_pal[1] - max_pal[0]):
                max_pal = pal
        return s[max_pal[0]:max_pal[1]+1]

#s = Solution()
#print(s.longestPalindrome("ababd"))
        

