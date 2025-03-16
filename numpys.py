#!/usr/bin/python3


import numpy as np
import time

# array_5x5 = [np.random.randint(1, 101) for _ in range(5)]
# print(array_5x5)
array_5x5 = [[np.random.randint(1, 101) for _ in range(5)] for _ in range(5)]
mean = np.mean(array_5x5)
std_dev = np.std(array_5x5)
print(mean, std_dev)
print(array_5x5)

# 2. Generate two 3x3 matrices of random numbers between 100 and 200
matrix_A = [[np.random.randint(100, 201) for _ in range(3)] for _ in range(3)]
matrix_B = np.random.randint(100, 201, (3, 3))

start = time.time()
result_np = np.dot(matrix_A, matrix_B)
end = time.time()


def manualMatrixmult(A, B):
    result = np.zeros(
        (A.shape[0], B.shape[1]), dtype=int
    )  # zeros is a calloced array and shape is a tuple on the arrays dimentions
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                result[i, j] += A[i, k] * B[k, j]
    return result


start_time_manual = time.time()
result_manual = manualMatrixmult(matrix_A, matrix_B)
end_time_manual = time.time()
