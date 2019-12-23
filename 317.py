import queue

class Solution:
    def shortestDistance(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        distance = [[0 for i in range(n)] for j in range(m)]
        buildings = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        lands = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 0]
        max_len = (m * n) ** 2
        if not lands:
            return -1

        que = queue.Queue()
        def update(i,j, value):
            if -1 < i < m and -1 < j < n and grid[i][j] == 0 and temp[i][j] == 0:
                temp[i][j] = value
                distance[i][j] += value
                que.put((i,j))
    

        for i, j in buildings:
            temp = [[0 for i in range(n)] for j in range(m)]
            que = queue.Queue()
            que.put((i,j))
            while not que.empty():
                i, j = que.get()
                update(i+1,j,temp[i][j]+1)
                update(i,j+1,temp[i][j]+1)
                update(i-1,j,temp[i][j]+1)
                update(i,j-1,temp[i][j]+1)
            for p, q in lands:
                if temp[p][q] == 0:
                    distance[p][q] = max_len
    
        min_len = max_len
        for p, q in lands:
            min_len = min(min_len, distance[p][q])
        if min_len >= max_len:
            return -1
        return min_len

#Solution().shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])