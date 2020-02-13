import multiprocessing as mp
from sort import Sort

class BitonicSort(Sort):
    def __init__(self, array, up):
        print("BitonicSorter is initialized")
        self.items = array
        print("BitonicSorter items: {}".format(self.items))
        print("BitonicSorter array: {}".format(array))
        self.order = up

    def sort(self):
        print("Overwriting Sort ABC")
        print(self.items)
        return self.items


def main():
    A = [4, 3, 2, 1]
    Q = BitonicSort(A, True)
    Q.sort()


if __name__ == '__main__':
    main()
