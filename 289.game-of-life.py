#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                neighbour = self.surround(board, i, j)
                if board[i][j] % 2 == 0:
                    if neighbour == 3:
                        board[i][j] = 2
                else:
                    if neighbour == 2 or neighbour == 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] >> 1

    def surround(self, board, i, j):
        m = len(board)
        n = len(board[0])
        neighbour = 0
        for p in range(max(0, i-1), min(m, i+2)):
            for q in range(max(0, j-1), min(n, j+2)):
                if p!=i or q!=j:
                    neighbour += board[p][q] % 2
        return neighbour

#Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
