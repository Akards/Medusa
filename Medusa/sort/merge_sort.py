import multiprocessing as mp
import os
from Medusa.sort import Sort
#from sort import sort

class Merge(Sort):
    def __init__(self, a, up, num_p):
        # Initiate variables
        self.items = a
        self.order = up 
        self.num_p = num_p
        self.procs = []
        self.arr_of_a = []
        self.arr_of_q = []

    def sort(self):
        '''
        Merge sort driver function.

        Args: 
            N/A

        Returns:
            A sorted version of array self.items
        '''

        div = len(self.items) // self.num_p
        q = mp.Queue()
        
        # Save work
        if len(self.items) == 0 or len(self.items) == 1:
            return self.items
    
        # Save more work
        if self.num_p == 1:
            self.merge_sort(self.items, q, len(self.items))
            self.items = q.get()
            return self.items

        #print("Original Array: {}".format(self.items))

        # Divide array among processes
        for i in range(self.num_p):
            self.arr_of_a.append(self.items[i*div:(i+1)*div])
        # Add any remaining elements to the end of the last process's subarray
        if len(self.items) % self.num_p != 0:
            self.arr_of_a[self.num_p-1].extend(self.items[div*self.num_p:])
        
        #print("Arr_of_a: {}".format(self.arr_of_a))

        # Create and start processes
        for p in range(self.num_p):
            size = len(self.arr_of_a[p])
            temp = mp.Process(target=self.merge_sort, args=(self.arr_of_a[p], q, size,))
            self.procs.append(temp)
            temp.start()
      
        # Wait for spawned processes to end
        for p in self.procs:
            p.join()

        # Replace old arr_of_a with sorted sublists
        for i in range(len(self.arr_of_a)):
            self.arr_of_a[i] = q.get()

        #print("New arr_of_a: {}".format(self.arr_of_a))
        
        # If there is only 1 process, the array is already fully sorted
        if self.num_p == 1:
            self.items = q.get()
            return self.items
        
        # Now merge sorted sublists
        self.procs = []
        #arr_of_q = []
        q_index = -1
        size = len(self.items)
        for p in range(self.num_p):
            if (p % 2 == 0):
                q2 = mp.Queue()
                self.arr_of_q.append(q2)
                q_index += 1
            temp = mp.Process(target=self.final_merge, args=(self.arr_of_a[p], 
                              self.num_p, p, self.arr_of_q, q_index, size,))
            self.procs.append(temp)
            temp.start()

        for p in self.procs:
            p.join()

        self.items = self.arr_of_q[0].get()
        return self.items

    def merge_sort(self, a, q, size):
        '''
        Sequential merge sort algorithm, called by each process on a subarray

        Args:
            a: the array or subarray to be sorted
            q: the queue that the processes will use to communicate w/ each other
            size: the size of a when it was first passed to merge_sort() in start()
            
        Returns:
            N/A
        '''

        if (len(a) > 1):
            # Divide the array into two halves
            mid = len(a) // 2
            left = a[:mid]
            right = a[mid:]
            
            # Repeat division until arrays are of size 1
            self.merge_sort(left, q, size)
            self.merge_sort(right, q, size)
            
            #print("Left: {}".format(left))
            #print("Right: {}".format(right))
            
            # Merge subarrays
            self.merge(a, left, right, q = q, size = size)
        elif len(a) == 1 and size == 1:
            q.put(a)

    def merge(self, a, left, right, **kwargs):
        '''
        Each process merges subarrays until it has its original subarray sorted

        Args:
            a: unsorted array that will be overwritten to hold the fully sorted array
            left: left subarray to merge
            right: right subarray to merge
            self.order: if true, sort array in ascending order, else in descending order
            q (optional): queue that processes will use to store their sorted subarray a
            size (optional): size of process's original subarray before it was divided up 

        Returns:
            N/A
        '''

        q = kwargs.get('q', None)
        size = kwargs.get('size', None)

        i = j = k = 0

        # Merge together
        while i < len(left) and j < len(right):
            if (left[i] < right[j]) == self.order:
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

        # If list has been fully sorted, add to queue
        if len(a) == size and q:
            #print(a)
            q.put(a)

    
    def final_merge(self, a, num_p, proc_id, queues, q_index, size):
        '''
        Once each process has sorted its assigned subarray, odd processes will merge their
        subarray with an even partner process's subarray until process 1 has fully sorted array

        Args:
            a: a process's subarray that is to be merged
            num_p: number of processes, will decrease as processes merge subarrays
            proc_id: process id, will change as other processes terminate
            queues: array of queues used by all processes to pass subarrays between each other
            q_index: index in queues array that refers to a particular process's queue
            size: size of array originally passed by the user to be sorted

        Returns:
            N/A
        '''

        if len(a) != size:
            # Handle edge case when there is an odd # of processes for merging last ranked proc
            if num_p % 2 != 0:
                if proc_id == num_p - 1:
                    #print("Process {} waiting until num_p ({}) is even".format(proc_id, num_p))
                    proc_id = proc_id // 2
                    num_p -= proc_id
                    q_index = proc_id // 2
                    self.final_merge(a, num_p, proc_id, queues, q_index, size) 
                    return
            # If even, add your subarray to odd partner's queue
            if proc_id % 2 == 0:
                #print("Process {} adding to queue {}".format(proc_id, q_index))
                queues[q_index].put(a)
                return
            # Else, merge your subarray w/ subarray added by even partner to your queue
            else:
                #print("Process {} merging...".format(proc_id))
                left = queues[q_index].get()    # From partner process
                right = a                       # From this process
                #print("Left: {}".format(left))
                #print("Right: {}".format(right))
                a = [None] * (len(left) + len(right))
                self.merge(a, left, right)
                proc_id = proc_id // 2
                q_index = proc_id // 2
                #print("Left and Right merged: {}".format(a))
                # Change num_p to reflect terminated even procs                
                if num_p % 2 == 0:
                    num_p = num_p // 2
                else:
                    num_p = (num_p // 2) + 1 

                self.final_merge(a, num_p, proc_id, queues, q_index, size)
        else:
            #print("Result after final merge:{}".format(a))
            queues[0].put(a)
'''
def main():
    A = [8, 9, 2, 5, 1, 7, 3, 4, 6]
    B = [8, 6, 2, 4, 1, 3, 5, 7]
    
    merge = Merge(A, True, 1)
    C = merge.sort()
    print(C)






if __name__ == "__main__":
    main()
'''
