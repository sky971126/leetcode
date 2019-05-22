#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
import math
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        M = len(matrix)
        N = len(matrix[0])
        results = []
        i = 0
        j = 0
        while i < math.ceil(M/2) and i < math.ceil(N/2):
            one_row_left = (M - 2 * i) == 1
            one_column_left = (N - 2 * i) == 1
            for n in range(i, N-i):
                results.append(matrix[i][n])
            for m in range(i+1, M-i-1):
                results.append(matrix[m][N-1-i])
            if not one_row_left:
                for n in range(N-1-i, i-1, -1):
                    results.append(matrix[M-1-i][n])
            if not one_column_left:
                for m in range(M-2-i, i, -1):
                    results.append(matrix[m][i])
            i += 1
        return results
#print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
