#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        for i in range(n//2):
            for j in range(i, n-i):
                matrix[i][j] = num
                num += 1
            for j in range(i+1, n-i-1):
                matrix[j][n-1-i] = num
                num += 1
            for j in range(n-i-1, i-1, -1):
                matrix[n-1-i][j] = num
                num += 1
            for j in range(n-i-2, i, -1):
                matrix[j][i] = num
                num += 1
        if n % 2 == 1:
            matrix[n//2][n//2] = num
        return matrix
# @lc code=end

print(Solution().generateMatrix(4))