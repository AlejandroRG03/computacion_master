
import numpy as np
from Matrix import Matrix

def inputs():
    A = Matrix(list(np.random.uniform(-1, 1, (3, 3))))
    B = Matrix(list(np.random.uniform(-1, 1, (3, 3))))
    return A, B

def test_Matrix_add():

    A, B = inputs()
    null = A * 0
    assert A + B == B + A
    assert A + null == A
    assert A + (A + B) == (A + A) + B

def test_Matrix_sub():

    A, B = inputs()
    assert A - B == -(B - A)
    assert A - B == A + (-B)

def test_Matrix_mul():

    A, _ = inputs()
    assert A * 0 == A * 0
    assert A * 1 == A
    assert 2 * A == A * 2
    assert (A * 2) / 2 == A

    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[2, 0], [1, 2]])
    C = Matrix([[4, 4], [10, 8]])

    assert A * B == C

def test_Matrix_transpose():

    A, _ = inputs()
    AT = A.T()
    m, n = A.shape()
    for i in range(m):
        for j in range(n):
            assert A[i, j] == AT[j, i]

def test_Matrix_get_set():

    A = Matrix([[0, 0], [0, 0]])
    A[0, 1] = 5

    assert A[0, 1] == 5


def test_matrix_shape_len():

    A = Matrix([[1, 2, 3], [4, 5, 6]])

    assert A.shape() == (2, 3)
    assert len(A) == 2

