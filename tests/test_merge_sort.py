#!/usr/bin/env python3
import unittest
import os
import math
import Medusa.Sort
from Medusa.Sort.MergeSort import *

class TestMergeSort(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("hello")

    def test_empty_list(self):
       A = []
       merge = Merge(A, 1)
       B = merge.begin_merge()
       self.assertEqual(B, [])

    def test_even_length_list_sequential_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, 1)
        B = merge.begin_merge()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_even_length_list_parallel_2_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, 2)
        B = merge.begin_merge()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_even_length_list_parallel_3_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, 3)
        B = merge.begin_merge()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_even_length_list_parallel_4_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, 4)
        B = merge.begin_merge()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_even_length_list_parallel_5_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, 5)
        B = merge.begin_merge()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_even_length_list_parallel_6_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, 6)
        B = merge.begin_merge()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_even_length_list_parallel_7_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, 7)
        B = merge.begin_merge()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_even_length_list_parallel_8_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, 8)
        B = merge.begin_merge()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_odd_length_list_sequential_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, 1)
        B = merge.begin_merge()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def test_odd_length_list_parallel_2_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, 2)
        B = merge.begin_merge()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])
  
    def test_odd_length_list_parallel_3_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, 3)
        B = merge.begin_merge()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])
 
    def test_odd_length_list_parallel_4_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, 4)
        B = merge.begin_merge()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])
 
    def test_odd_length_list_parallel_5_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, 5)
        B = merge.begin_merge()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def test_odd_length_list_parallel_7_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, 7)
        B = merge.begin_merge()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def test_odd_length_list_parallel_8_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, 8)
        B = merge.begin_merge()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def test_odd_length_list_parallel_9_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, 9)
        B = merge.begin_merge()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])




















