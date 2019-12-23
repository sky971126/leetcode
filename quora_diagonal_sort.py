def solution(A):
    N = len(A)
    def sort_diagonal(i,j): #i, j is the starting index of the diagonal line
        to_sort = []
        while (i<N and j<N):
            to_sort.append(A[i][j])
            i += 1
            j += 1
        i -= 1
        j -= 1
        to_sort.sort()
        while (i>-1 and j>-1):
            A[i][j] = to_sort.pop()
            i -= 1
            j -= 1
    for i in range(N):
        sort_diagonal(i,0)
    for i in range(1,N):
        sort_diagonal(0,i)
    return A

print(solution([[8, 4, 1],[4, 4, 1],[4, 8, 9]]))