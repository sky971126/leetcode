#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        N = len(matrix[0])
        results = []
        i = 0
        j = 0
        while i <= M//2 and i <= N//2:
            one_row_left = (M//2 - 2 * i) == 1
            one_column_left = (N//2 - 2 * i) == 1
            for m in range(i, M-i):
                results.append(matrix[i][m])
            for n in range(i+1, M-i-1):
                results.append(matrix[M-1-i][n])
            if not one_row_left:
                for m in range(M-1-i, i-1, -1):
                    results.append(matrix[N-1-i][m])
            if one_column_left:
            else:

            i += 1
