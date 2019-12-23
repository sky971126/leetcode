import queue
class Solution:
    def numDistinctIslands(self, grid) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        ht = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                que = queue.Queue()
                que.put((i,j))
                grid[i][j] = 0
                path = []
                while not que.empty():
                    p, q = que.get()
                    if -1 < p+1 < m and -1 < q < n and grid[p+1][q] == 1:
                        path.append((p+1-i,q-j))
                        que.put((p+1,q))
                        grid[p+1][q] = 0
                    if -1 < p-1 < m and -1 < q < n and grid[p-1][q] == 1:
                        path.append((p-1-i,q-j))
                        que.put((p-1,q))
                        grid[p-1][q] = 0
                    if -1 < p < m and -1 < q-1 < n and grid[p][q-1] == 1:
                        path.append((p-i,q-1-j))
                        que.put((p,q-1))
                        grid[p][q-1] = 0
                    if -1 < p < m and -1 < q+1 < n and grid[p][q+1] == 1:
                        path.append((p-i,q+1-j))
                        que.put((p,q+1))
                        grid[p][q+1] = 0
                ht.add(tuple(path))
        return len(ht)

Solution().numDistinctIslands([[1,1,0],[0,1,1],[0,0,0],[1,1,1],[0,1,0]])