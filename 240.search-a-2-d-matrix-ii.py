#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        col_l = 0
        col_r = len(matrix[0]) - 1
        while (col_l <= col_r):
            m = (col_l + col_r) // 2
            if matrix[0][m] == target:
                return True
            elif matrix[0][m] < target:
                col_l = m + 1
            else:
                col_r = m - 1
        col_r_bound = col_r
        col_l = 0
        col_r = len(matrix[0]) - 1
        while (col_l <= col_r):
            m = (col_l + col_r) // 2
            if matrix[-1][m] == target:
                return True
            elif matrix[-1][m] < target:
                col_l = m + 1
            else:
                col_r = m - 1
        col_l_bound = col_l
        for col in range(col_l_bound, col_r_bound+1):
            row_l = 0
            row_r = len(matrix) - 1
            while (row_l <= row_r):
                m = (row_l + row_r) // 2
                if matrix[m][col] == target:
                    return True
                elif matrix[m][col] < target:
                    row_l = m + 1
                else:
                    row_r = m - 1

        return False
    """
    # def searchMatrix(self, matrix, target):
    #     if not matrix:
    #         return False
    #     row = 0
    #     col = len(matrix[0]) - 1
    #     while(-1 < row < len(matrix) and -1 < col < len(matrix[0])):
    #         if matrix[row][col] == target:
    #             return True
    #         elif matrix[row][col] < target:
    #             row += 1
    #         else:
    #             col -= 1
    #     return False



    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while (-1<i<m and -1<j<n):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False



#Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
            

# @lc code=end

