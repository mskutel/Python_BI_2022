#!/usr/bin/env python
import numpy as np

if __name__ == "__main__":
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.random.normal(size=(3, 4))
    arr3 = np.arange(11, 20).reshape(3, 3)


def matrix_multiplication(mat1, mat2):
    return np.matmul(mat1, mat2)


def multiplication_check(matrices):
    for i in range(len(matrices) - 1):
        if np.shape(matrices[i])[1] == np.shape(matrices[i + 1])[0]:
            pass
        else:
            return False
    return True


def multiply_matrices(matrices):
    if multiplication_check(matrices):
        for i in range(len(matrices) - 1):
            matrices[i + 1] = np.matmul(matrices[i], matrices[i + 1])
        return matrices[-1]
    else:
        return None


def compute_2d_distance(point1, point2):
    if np.shape(point1)[0] > 2:
        return 'It\'s not a 2d space'
    else:
        return np.sqrt(np.sum((point1 - point2) ** 2))


# Ради интереса другая форма:
def compute_multidimensional_distance(point1, point2):
    return np.linalg.norm(point1 - point2)


def compute_pair_distances(array):
    i, j = np.meshgrid(array, array)
    return abs(i - j)
