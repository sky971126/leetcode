class Solution:
    def numIslands2(self, m: int, n: int, positions) :
        roots2level = {}
        lands2roots = {}
        res = []
        num = 0
        def find(pos):
            while lands2roots[pos] != pos:
                pos = lands2roots[pos]
            return pos
        def union(pos1, pos2):
            root1, root2 = find(pos1), find(pos2)
            lands2roots[pos1] = root1
            lands2roots[pos2] = root2
            if root1 == root2:
                return False
            if roots2level[root1] < roots2level[root2]:
                lands2roots[root1] = root2
            else:
                lands2roots[root2] = root1
                if roots2level[root1] == roots2level[root2]:
                    roots2level[root1] += 1
            return True
        for pos in positions:
            i, j = pos
            pos = tuple(pos)
            if pos in lands2roots:
                res.append(num)
                continue
            num += 1
            roots2level[pos] = 0
            lands2roots[pos] = pos
            if (i+1, j) in lands2roots:
                if union((i+1,j), pos):
                    num -= 1
            if (i-1, j) in lands2roots:
                if union((i-1,j), pos):
                    num -= 1           
            if (i, j+1) in lands2roots:
                if union((i,j+1), pos):
                    num -= 1
            if (i, j-1) in lands2roots:
                if union((i,j-1), pos):
                    num -= 1
            res.append(num)
            #print(lands2roots)
        return res
print(Solution().numIslands2(2,2,[[0,0],[1,1],[0,1]]))