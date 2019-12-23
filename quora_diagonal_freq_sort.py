import itertools
import collections

def solution(A):
    n = len(A)
    A_flat = list(itertools.chain.from_iterable(A))
    A_count = [[i,j] for i,j in collections.Counter(A_flat).items()]
    A_count.sort(key=lambda x: (x[1], x[0]), reverse=True)
    def diagonal(i,j): # starting index
        while A_count:
            if -1 < i < n and -1 < j < n:
                A[i][j] = A_count[-1][0]
                A_count[-1][1] -= 1
                if A_count[-1][1] == 0:
                    A_count.pop()
                i -= 1
                j += 1
            else:
                return
    for i in range(n-1,-1,-1):
        diagonal(n-1,i)
        print(n-1,i)
    for i in range(n-2,-1,-1):
        diagonal(i,0)
        print(i,0)
A = [[1,1,2],[2,3,3],[3,3,4]]
solution(A)
print(A)