def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N//2):
            for j in range(N-1-2*i):
                if i != j and i!=N-1-j:
                    matrix[i][i+j], matrix[i+j][N-1-i], matrix[N-1-i][N-1-i-j], matrix[N-1-i-j][i] = \
                        matrix[N-1-i-j][i], matrix[i][i+j], matrix[i+j][N-1-i], matrix[N-1-i][N-1-i-j]
    
matrix = [[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25]]

rotate(matrix)
print(matrix)