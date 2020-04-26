#!/usr/bin/env python3
import unittest
import Medusa.Sort
from random import shuffle
from Medusa.Sort.BitonicSort import *

class TestBitonicSort(unittest.TestCase):
    def test_empty_list(self):
       A = []
       Q = BitonicSort(A, True, 1)
       B = Q.sort()
       self.assertEqual(B, [])

    def test_sequential_bitonic_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        Q = BitonicSort(A, True, 1)
        B = Q.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_parallel_same_amount_of_procs(self):
        A = [4, 2, 1, 3]
        Q = BitonicSort(A, True, 4)
        B = Q.sort()
        self.assertEqual(B, [1, 2, 3, 4])

    def test_parallel_2_bitonic_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        Q = BitonicSort(A, True, 2)
        B = Q.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_parallel_2_bitonic_sort_reverse(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        Q = BitonicSort(A, False, 2)
        B = Q.sort()
        self.assertEqual(B, [8, 7, 6, 5, 4, 3, 2, 1])

    def test_parallel_4_bitonic_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        Q = BitonicSort(A, True, 4)
        B = Q.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_parallel_4_bitonic_sort_reverse(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        Q = BitonicSort(A, False, 4)
        B = Q.sort()
        self.assertEqual(B, [8, 7, 6, 5, 4, 3, 2, 1])

    def test_parallel_8_bitonic_sort(self):
        A = [4, 15, 2, 11, 12, 7, 6, 3, 5, 9, 0, 8, 14, 13, 10, 1]
        Q = BitonicSort(A, True, 8)
        B = Q.sort()
        self.assertEqual(B, [i for i in range(16)])

    def test_parallel_8_bitonic_sort_large(self):
        A = [i for i in range(128)]
        shuffle(A)
        Q = BitonicSort(A, True, 8)
        B = Q.sort()
        self.assertEqual(B, [i for i in range(128)])

    def test_parallel_16_bitonic_sort_very_large(self):
        A = [i for i in range(4096)]
        shuffle(A)
        Q = BitonicSort(A, True, 16)
        B = Q.sort()
        self.assertEqual(B, [i for i in range(4096)])
    """
    TODO: missing tests
    1. Test large list (N = 128)
    2. Test larger list (N = 1024)
    3. Test list where (N != 2**k), where k is a natural number
    """
