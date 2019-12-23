#
# @lc app=leetcode id=730 lang=python3
#
# [730] Count Different Palindromic Subsequences
#
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        DP = []
        N = len(S)
        for _ in range(4):
            temp = []
            for _ in range(N):
                temp.append([0]*N)
            DP.append(temp)
        
        for j in range(N):
            for i in range(j,-1,-1):
                for k in range(4):
                    if i == j:
                        if self.getk(S[j]) == k:
                            DP[k][i][j] = 1
                    else:
                        if self.getk(S[i]) == k and self.getk(S[j]) == k:
                            if j == i+1:
                                DP[k][i][j] = 2
                            else:
                                for p in range(4):
                                    if i==0 and j==5:
                                        print(DP[p][i+1][j-1])
                                    DP[k][i][j] += DP[p][i+1][j-1]
                                DP[k][i][j] += 2
                        elif self.getk(S[j]) == k:
                            DP[k][i][j] = DP[k][i+1][j]
                        else:
                            DP[k][i][j] = DP[k][i][j-1]
        res = 0
        for k in range(4):
            res += DP[k][0][N-1]
        return res % (pow(10,9)+7)

    def getk(self, c):
        return ord(c) - 97
print(Solution().countPalindromicSubsequences("bbccbb"))
