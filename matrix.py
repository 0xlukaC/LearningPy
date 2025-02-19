#!/usr/bin/python3


# matrix multiplication
def multiply(mat1, mat2):
    # check if rows == columns
    if len(mat1[0]) != len(mat2):
        return None

    rown = len(mat1)
    coln = len(mat1[0])
    sharedd = len(mat2[0])

    arr = [[0] * sharedd for _ in range(rown)]
    # arr = [[0] * coln for _ in range(rown)]  # rown * coln
    for i in range(rown):
        for j in range(sharedd):
            for s in range(coln):
                arr[i][j] += mat1[i][s] * mat2[s][j]
    return arr


mat1 = [[1, 2], [3, 4]]

mat2 = [[5, 6], [7, 8]]

mat3 = [[1, 2, 3], [4, 5, 6]]

mat4 = [[7, 8], [9, 10], [11, 12]]

print(multiply(mat1, mat2))

print(multiply(mat3, mat2))

print(multiply(mat3, mat4))
