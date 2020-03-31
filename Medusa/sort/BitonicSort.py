import random
import multiprocessing as mp
from sort import Sort

class BitonicSort(Sort):
    def __init__(self, array, up):
        self.items = array
        self.order = up

    def sort(self):
        """
        Bitonic sort. Parallelized sort algorithm that runs in O(log^2(n))

        Args:
            array: the list to be sorted
            up: if True list is sorted in ascending order, if False list is
            sorted in descending order

        Returns:
            A sorted sequence of numbers.
        """
        if len(self.items) <= 1:
            return self.items
        else:
            left = BitonicSort(self.items[:len(self.items)//2], True)
            left.sort()
            right = BitonicSort(self.items[len(self.items)//2:], False)
            right.sort()
            self.items = self.merge(left.items + right.items)
            return self.items

    def merge(self, A):
        if len(A) == 1:
            return A
        else:
            self.compare(A)
            left = self.merge(A[:len(A) // 2])
            right = self.merge(A[len(A) // 2:])
            return left + right

    def compare(self, A):
        dist = len(A) // 2
        for i in range(dist):
            if (A[i] > A[i + dist]) == self.order:
                A[i], A[i + dist] = A[i + dist], A[i]

def is_ordered(A):
    size = len(A)
    for i in range(size-1):
        if A[i] > A[i+1]:
            return False
    return True

def main():
    for list_size in range(4, 17):
        print("Lists of size {}".format(list_size))
        pos = 0
        neg = 0
        for i in range(1000):
            A = [random.randint(0, 100) for i in range(list_size)]
            Q = BitonicSort(A, True);
            Q.sort()
            if is_ordered(Q.items):
                pos += 1
            else:
                neg += 1
        print("There were {} positive results".format(pos))
        print("There were {} negative results".format(neg))
        print("="*30+"\n")


if __name__ == '__main__':
    main()
