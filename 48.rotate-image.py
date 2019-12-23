#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        for i in range(N//2):
            for j in range(N-1-2*i):
                matrix[i][i+j], matrix[i+j][N-1-i], matrix[N-1-i][N-1-i-j], matrix[N-1-i-j][i] = \
                    matrix[N-1-i-j][i], matrix[i][i+j], matrix[i+j][N-1-i], matrix[N-1-i][N-1-i-j]

class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(1,n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

"""
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n//2):
            for j in range(n-2*i-1):
                temp = matrix[i][i+j]
                matrix[i][i+j] = matrix[n-1-i-j][i]
                matrix[n-1-i-j][i] = matrix[n-1-i][n-1-i-j]
                matrix[n-1-i][n-1-i-j] = matrix[i+j][n-1-i]
                matrix[i+j][n-1-i] = temp

# @lc code=end
