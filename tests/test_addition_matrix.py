#!/usr/bin/env python3
import unittest
import numpy as np
import Medusa.matrix
from Medusa.matrix.addition import add

class TestMatrixAddition(unittest.TestCase):
    def test_add_if_A_not_2d(self):
        A = np.array([1,2,3])
        B = np.array([[3,4,5],[0,1,0]])
        with self.assertRaises(Exception) as ctx:
            add(A, B, 1)
        self.assertTrue('Must provide 2-dimensional matrix. Matrix A has 1 dimensions' in str(ctx.exception))

    def test_add_if_B_not_2d(self):
        A = np.array([[3,4,5],[0,1,0]])
        B = np.array([1,2,3])
        with self.assertRaises(Exception) as ctx:
            add(A, B, 1)
        self.assertTrue('Must provide 2-dimensional matrix. Matrix B has 1 dimensions' in str(ctx.exception))

    def test_add_improper_sized_inputs(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[1, 2, 3], [2, 2, 5]])
        with self.assertRaises(Exception) as ctx:
            add(A, B, 1)
        self.assertTrue('Must provide 2-dimensional matrices with equivalent number of rows and columns', str(ctx.exception))

    def test_add_matrix_sequentially(self):
        A = np.array([[1, 0, 1], [0, 1, 0]])
        B = np.array([[0, 1, 0], [1, 0, 1]])
        C = add(A, B, 1)
        self.assertTrue(np.allclose(C, np.array([[1,1,1],[1,1,1]])))

    def test_add_matrix_4_parallel(self):
        A = np.array([[1, 0, 1], [0, 1, 0], [0, 0, 0]])
        B = np.array([[0, 1, 0], [1, 0, 1], [1, 1, 1]])
        C = add(A, B, 4)
        self.assertTrue(np.allclose(C, np.array([[1,1,1],[1,1,1],[1,1,1]])))

    def test_add_matrix_8_parallel(self):
        A = np.arange(50).reshape((10, 5))
        B = np.arange(50).reshape((10, 5))
        C = add(A, B, 8)
        self.assertTrue(np.allclose(C, np.add(A, B)))

    def test_add_matrix_16_parallel(self):
        A = np.arange(50).reshape((10, 5))
        B = np.arange(50).reshape((10, 5))
        C = add(A, B, 16)
        self.assertTrue(np.allclose(C, np.add(A, B)))

    def test_add_matrix_with_negative_values(self):
        A = np.array([[-1, -2], [0, 2]])
        B = np.array([[2, -3], [-1, 3]])
        C = add(A, B, 1)
        self.assertTrue(np.allclose(C, np.array([[1, -5], [-1, 5]])))
