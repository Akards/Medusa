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
       merge = Merge(A, True, 1)
       B = merge.sort()
       self.assertEqual(B, [])
    
    def test_even_length_list_sequential_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, True, 1)
        B = merge.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])
        
    def test_even_length_list_parallel_2_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, True, 2)
        B = merge.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_even_length_list_parallel_3_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, True, 3)
        B = merge.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_even_length_list_parallel_4_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, True, 4)
        B = merge.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_even_length_list_parallel_5_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, True, 5)
        B = merge.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_even_length_list_parallel_6_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, True, 6)
        B = merge.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_even_length_list_parallel_7_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, True, 7)
        B = merge.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_even_length_list_parallel_8_merge_sort(self):
        A = [8, 6, 7, 3, 5, 2, 1, 4]
        merge = Merge(A, True, 8)
        B = merge.sort()
        self.assertEqual(B, [1, 2, 3, 4, 5, 6, 7, 8])
    
    def test_odd_length_list_sequential_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, True, 1)
        B = merge.sort()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])
    
    def test_odd_length_list_parallel_2_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, True, 2)
        B = merge.sort()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def test_odd_length_list_parallel_3_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, True, 3)
        B = merge.sort()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def test_odd_length_list_parallel_4_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, True, 4)
        B = merge.sort()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def test_odd_length_list_parallel_5_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, True, 5)
        B = merge.sort()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])
    
    def test_odd_length_list_parallel_7_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, True, 7)
        B = merge.sort()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])
    
    def test_odd_length_list_parallel_8_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, True, 8)
        B = merge.sort()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])

    def test_odd_length_list_parallel_9_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, True, 9)
        B = merge.sort()
        self.assertEqual(B, [0, 1, 2, 3, 4, 6, 7, 8, 9])
   
    def test_even_length_list_parallel_4_decreasing_order_merge_sort(self):
        A = [4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, False, 4)
        B = merge.sort()
        self.assertEqual(B, [8, 7, 6, 4, 3, 2, 1, 0])

    def test_odd_length_list_parallel_4_decreasing_order_merge_sort(self):
        A = [9, 4, 3, 7, 2, 1, 8, 0, 6]
        merge = Merge(A, False, 4)
        B = merge.sort()
        self.assertEqual(B, [9, 8, 7, 6, 4, 3, 2, 1, 0])

















