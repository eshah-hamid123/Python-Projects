matrix1 = [
    [1 , 2, 3],
    [4 ,4 ,5],
    [6, 7, 8]
]
matrix2 = [
    [3 , 5, 5],
    [4 ,2 ,2],
    [1, 3, 3]
]
result = [
    [0 , 0, 0],
    [0 ,0 ,0],
    [0, 0, 0]
]
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
for r in result:
    print(r)