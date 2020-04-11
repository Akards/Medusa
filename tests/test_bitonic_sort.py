#!/usr/bin/env python3
import unittest
import filecmp
import sys
import os
import math
import Medusa.sort
from Medusa.sort.Par_BitonicSort import *

class TestBitonicSort(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("hello")

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

    def test_parallel_2_bitonic_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        Q = BitonicSort(A, True, 2)
        B = Q.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_parallel_4_bitonic_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        Q = BitonicSort(A, True, 4)
        B = Q.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_parallel_8_bitonic_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        Q = BitonicSort(A, True, 8)
        B = Q.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])
