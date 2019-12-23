#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    """ O(m2n2)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        def leftup(i,j):
            res = 0
            for k in range(min(m-i,n-j)):
                for p in range(i, i+k+1):
                    if matrix[p][j+k] == "0":
                        return res
                for q in range(j, j+k+1):
                    if matrix[i+k][q] == "0":
                        return res
                res = (k+1)**2
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, leftup(i,j))
        return res
    """
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        DP = [0] * n
        res = 0
        for i in range(m):
            last = 0
            for j in range(n):
                if matrix[i][j] == "0":
                    DP[j] = 0
                    continue
                temp = DP[j]
                DP[j] = min(DP[j-1], DP[j], last) + 1
                last = temp
                res = max(res, DP[j])
        return res ** 2
        

# @lc code=end

Solution().maximalSquare([["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]])

