#!/usr/bin/env python3
import unittest
import numpy as np
import Medusa.matrix
from Medusa.matrix.multiplication import multiply

class TestMatrixMultiplication(unittest.TestCase):
    def test_mult_if_A_not_2d(self):
        A = np.array([1,2,3])
        B = np.array([[3,4,5],[0,1,0]])
        with self.assertRaises(Exception) as ctx:
            multiply(A, B, 1)
        self.assertTrue('Must provide 2-dimensional matrix. Matrix A has 1 dimensions' in str(ctx.exception))

    def test_mult_if_B_not_2d(self):
        A = np.array([[3,4,5],[0,1,0]])
        B = np.array([1,2,3])
        with self.assertRaises(Exception) as ctx:
            multiply(A, B, 1)
        self.assertTrue('Must provide 2-dimensional matrix. Matrix B has 1 dimensions' in str(ctx.exception))

    def test_mult_improper_sized_inputs(self):
        A = np.array([[1, 2, 3],[4, 5, 6]])
        B = np.array([[1, 2, 3],[4, 5, 6]])
        with self.assertRaises(Exception) as ctx:
            multiply(A, B, 1)
        self.assertTrue('A (3x2) and B (3x2) row number does not match column number' in str(ctx.exception))

    def test_mult_sequential_execution(self):
        A = np.array([[-1, 4], [2, 3]])
        B = np.array([[9, -3], [6, 1]])
        C = multiply(A, B, 1)
        self.assertTrue(np.allclose(C, np.array([[15, 7], [36, -3]])))

    def test_mult_parallel_4_procs(self):
        A = np.array([[1, 2, 3, 4, 5] for i in range(5)])
        B = np.array([[i%2] for i in range(1, 6)])
        C = multiply(A, B, 4)
        print(A, "times", B, "=", C)
        self.assertTrue(np.allclose(C, np.array([[9] for i in range(5)])))

    def test_mult_parallel_8_procs(self):
        A = np.array([[1, -2, 3] for i in range(10)])
        B = np.array([[i+1] for i in range(3)])
        C = multiply(A, B, 4)
        self.assertTrue(np.allclose(C, np.array([[6] for i in range(10)])))

    def test_mult_by_identity_mtx(self):
        A = np.array([[i, i**2, i**3] for i in range(3)])
        B = np.array([[1, 0, 0],[0, 1, 0], [0, 0, 1]])
        C = multiply(A, B, 1)
        self.assertTrue(np.allclose(C, A))

