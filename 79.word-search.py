#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
class Solution:
    def dfs(self, board, i, j, index, word):
        if index >= len(word):
            return True
        m = len(board)
        n = len(board[0])
        if (i>-1) and (j>-1) and (i<m) and (j<n):
            if (board[i][j] == word[index]):
                board[i][j] = "0"
                if self.dfs(board, i+1, j, index+1, word):
                    return True
                if self.dfs(board, i, j+1, index+1, word):
                    return True
                if self.dfs(board, i-1, j, index+1, word):
                    return True
                if self.dfs(board, i, j-1, index+1, word):
                    return True
                board[i][j] = word[index]
        return False
            
    def exist(self, board, word):
        if len(board) == 0:
            return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, 0, word):
                    return True
        return False
#s = Solution()
#print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB"))
