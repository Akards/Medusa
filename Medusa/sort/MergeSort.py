import multiprocessing as mp
import os

class Merge():
    def __init__(self, a):
        self.a = a

    def mergeSort(self, a, q, size):
        if (len(a) > 1):
            # Divide the array into two halves
            mid = len(a) // 2
            left = a[:mid]
            right = a[mid:]

            self.mergeSort(left, q, size)
            self.mergeSort(right, q, size)

            #print("Left: {}".format(left))
            #print("Right: {}".format(right))

            i = j = k = 0

            # Merge together
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1
                k += 1

            # Capture any remaining elements
            while i < len(left):
                a[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                a[k] = right[j]
                j += 1
                k += 1
            #print(a)

        # If list has been fully sorted, add to queue
        if len(a) == size:
            #print(a)
            q.put(a)

    def merge(self, b, q):
        for i in range(10):
            q.put(i)

def printList(a):
    for i in range(len(a)):
        print(a[i]),
    print("")

def printQueue(q):
    print("Queue elements:")
    if q.qsize() == 0:
        print("Queue is empty")
        return
    while not q.empty():
        print(q.get()),
    print("")


def main():

    num_p = 3                               # # of processes
    #TODO Implement a numpy array to save memory space
    a = [3, 8, 6, 2, 1, 10, 2, 7, 4, 13, 6] # Array to sort
    q = mp.Queue()                             # Queue to store process return vals
    q2 = mp.Queue(maxsize=15)
    procs = []                              # Array of processes
    arr_of_a = []                           # Holds each process's subarray
    div = len(a) // num_p                   # Used to divide array a among procs

    # Divide array among available processes
    for i in range(num_p):
        arr_of_a.append(a[i*div:(i+1)*div])
    # Add any remaining elements to the end of the last process's subarray
    if len(a) % num_p != 0:
        arr_of_a[num_p-1].extend(a[div*num_p:])

    print(arr_of_a)

    # Create instance of Merge
    merge = Merge(a)

    # Create and start processes
    for p in range(num_p):
        size = len(arr_of_a[p])
        temp = mp.Process(target=merge.mergeSort, args=(arr_of_a[p], q, size,))
        procs.append(temp)
        temp.start()

    # Wait for spawned processes to end
    for p in procs:
        p.join()

    print(q.qsize())
    printQueue(q)


if __name__ == "__main__":
    main()

