import random
import math
import multiprocessing as mp
from Medusa.Sort import Sort

class BitonicSort(Sort):
    def __init__(self, array, up, proc_num):
        self.items = array
        self.size = len(array)
        self.order = up
        self.p = proc_num
        bitsize = int(math.log2(proc_num))
        self.proc_names = []
        for i in range(proc_num):
            name = "{0:b}".format(i)
            name = name.zfill(bitsize)
            self.proc_names.append(name)


    def sort(self):
        """
        Bitonic sort. Parallel sort algorithm that runs in O(log^2(n))

        Args:
            array: the list to be sorted
            up: if True list is sorted in ascending order, if False list is
            sorted in descending order

        Returns:
            A sorted sequence of numbers.
        """
        arr_size = len(self.items)
        slice_size = arr_size//self.p
        q = mp.Queue()
        proc_arr = []

        if arr_size == 0:
            return []
        # Spawn all necessary processors running merge sequentially on
        # different slices
        for i in range(len(self.proc_names)):
            bottom = i*slice_size
            top = (i+1)*slice_size
            print("My process got:", self.items[bottom:top])
            p = mp.Process(target=self.seq_bitonic_sort,
                           args=(self.items[bottom:top], self.order, q),
                           name=self.proc_names[i])
            proc_arr.append(p)
            p.start()

        # Wait for processes to terminate before merging
        for i in range(len(self.proc_names)):
            proc_arr[i].join()

        # Merges the results from each individual process
        proc_num = self.p//2
        proc_arr.clear()
        while proc_num > 0:
            for proc in range(proc_num):
                A = q.get()
                B = q.get()
                p = mp.Process(target=self.merge, args=(A, B, q))
                proc_arr.append(p)
                p.start()
            slice_size *= 2
            proc_num = proc_num // 2
            print("This is the total number of procs", proc_num)
            for i in range(len(proc_arr)):
                proc_arr[i].join()
            proc_arr.clear()

        answer = q.get()
        return answer

    def merge(self, A, B, q):
        size = len(A)
        print("="*60)
        print("This is A", A)
        print("This is B", B)
        C = [] # List to be populated with values from A and B
        j, k = 0, 0
        for i in range(size*2):
            if (A[j] < B[k]) == self.order:
                C.append(A[j])
                j += 1
                if j == size:
                    C += B[k:]
                    break
            else:
                C.append(B[k])
                k += 1
                if k == size:
                    C += A[j:]
                    break

        print("This is C", C)
        print("="*60)
        q.put(C)


    def seq_bitonic_sort(self, A, up, q):
        if len(A) <= 1:
            q.put(A)
            return A
        else:
            left = self.seq_bitonic_sort(A[:len(A) // 2], True, q)
            right = self.seq_bitonic_sort(A[len(A) // 2:], False, q)
            A = self.seq_merge(left+right, up)
            if len(A) == self.size/self.p:
                q.put(A)
            return A

    def seq_merge(self, A, up):
        """
        Sequential implementation of merge. Ran by each processor on their
        array slice.

        Args:
            A: array to be merged

        Returns:
            A merged array from two partitions
        """
        if len(A) == 1:
            return A
        else:
            self.compare(A, up)
            left = self.seq_merge(A[:len(A) // 2], up)
            right = self.seq_merge(A[len(A) // 2:], up)
            return left + right

    def compare(self, A, up):
        dist = len(A) // 2
        for i in range(dist):
            if (A[i] > A[i + dist]) == up:
                A[i], A[i + dist] = A[i + dist], A[i]

def is_ordered(A):
    size = len(A)
    for i in range(size-1):
        if A[i] > A[i+1]:
            return False
    return True
