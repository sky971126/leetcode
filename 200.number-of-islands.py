#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        res = 0
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    res += 1
                    self.numIslands_helper(grid, i, j)
        return res
    
    def numIslands_helper(self, grid, i, j):
        height = len(grid)
        width = len(grid[0])
        grid[i][j] = "-1"
        if i > 0 and grid[i-1][j] == "1":
            self.numIslands_helper(grid, i-1, j)
        if j > 0 and grid[i][j-1] == "1":
            self.numIslands_helper(grid, i, j-1)
        if i < height-1 and grid[i+1][j] == "1":
            self.numIslands_helper(grid, i+1, j)
        if j < width-1 and grid[i][j+1] == "1":
            self.numIslands_helper(grid, i, j+1)
        

