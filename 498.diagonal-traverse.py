#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []
        res = []
        def up(i, j):
            if -1 < i < len(matrix) and -1 < j < len(matrix[0]):
                res.append(matrix[i][j])
                up(i-1, j+1)
        def down(i, j):
            if -1 < i < len(matrix) and -1 < j < len(matrix[0]):
                down(i-1, j+1)
                res.append(matrix[i][j])
        m = len(matrix)
        n = len(matrix[0])
        flag_up = True

        for i in range(0,m):
            if flag_up:
                up(i, 0)
            else:
                down(i, 0)
            flag_up = not flag_up
    
        for i in range(1, n):
            if flag_up:
                up(m-1, i)
            else:
                down(m-1, i)
            flag_up = not flag_up
        
        return res



# @lc code=end
print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
