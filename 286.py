import queue

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = (1 << 31) - 1
        que = queue.Queue()
        m = len(rooms)
        n = len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    que.put((i,j))
        
        def update(i, j, value):
            if -1 < i < m and -1 < j < n and rooms[i][j] == INF:
                rooms[i][j] = value + 1
                que.put((i, j))

        while not que.empty():
            i, j = que.get()
            update(i+1, j, rooms[i][j])
            update(i, j+1, rooms[i][j])
            update(i-1, j, rooms[i][j])
            update(i, j-1, rooms[i][j])
        
        return rooms