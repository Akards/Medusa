import multiprocessing as mp
from math import log10, floor
from numpy import array
from sys import maxsize
from random import shuffle

from Medusa.sort import Sort

class Paradis(Sort):

    buckets = 0
    locks = []


    def __init__(self, buckets):
        #support for buckets != 10 is coming but not here yet
        self.buckets = buckets
        for i in range(buckets):
            self.locks.append(mp.Lock())

    def sort(self, num_procs):
        for b in range(self.buckets):
            self.sort_aux(num_procs, b)
        print("fin: ", self.items)

    def createLocalHistogram(self, begin, end, place, globalHistogram, localHistogram): #also merges local histogram w/ global
        # [begin, end)
        for i in range(end-begin):
            item = self.items[i + begin]
            if place >= len(str(item)):
                localHistogram[0] = localHistogram[0] + 1
                continue
            localHistogram[int(str(item)[::-1][place])] = localHistogram[int(str(item)[place])] + 1
        for i in range(self.buckets):
            self.locks[i].acquire()
            globalHistogram[i] = globalHistogram[i] + localHistogram[i]
            self.locks[i].release()
            

    def sort_aux(self, num_procs, place):
        globalHistogram = mp.Array('i', [0]*self.buckets, lock=False)
        localHistsArray = []
        for i in range(num_procs):
            localHistsArray.append(mp.Array('i', [0]*self.buckets, lock=False))
        procs = []

        for i in range(num_procs):
            begin = (len(self.items) // num_procs) * i
            end = 0
            if (i == num_procs-1):
                end = len(self.items)
            else:
                end = begin + (len(self.items) // num_procs)
            procs.append(mp.Process(target=self.createLocalHistogram, args=(begin, end, place, globalHistogram, localHistsArray[i])))

        for i in procs:
            i.start()
        for i in procs:
            i.join()
        for i in range(1, self.buckets):
            globalHistogram[i] = globalHistogram[i] + globalHistogram[i-1]

        self.lazy_distribute(globalHistogram, place)
#        procs = []
#        for i in range(num_procs):
#            begin = (len(self.items) // num_procs) * i
#            end = 0
#            if (i == num_procs-1):
#                end = len(self.items)
#            else:
#                end = begin + (len(self.items) // num_procs)
#            procs.append(mp.Process(target=self.distribute, args=(begin, end, place, globalHistogram, localHistsArray, newItems, i)))
#        for i in procs:
#            i.start()
#        for i in procs:
#            i.join()
#        for i in range(len(self.items)):
#            print(newItems[i])


    def lazy_distribute(self, globalHistogram, place): #todo fix this
        newItems = [0]*len(self.items)
        for i in range(len(self.items)):
            index = len(self.items)-i-1
            p = 0
            item = self.items[index]
            if place < len(str(item)):
                p = int(str(item)[place])
            print(p)
            offset = globalHistogram[p]-1
            newItems[offset] = item
            globalHistogram[p] = globalHistogram[p]-1
        self.items = newItems
        
            

    def distribute(self, begin, end, place, globalHistogram, LocalHists, newItems, processNumber): #still parallel but not as cool as paradis.
        #todo replace this with paradis partition/permute/repair
        offset = []
        for i in range(self.buckets):
            prevSum = 0
            for x in range(processNumber-1):
                prevSum = prevSum + LocalHists[x][place]
            offset.append(prevSum)
        for i in range(self.buckets):
            offset[i] = offset[i] + globalHistogram[i]
        for i in range(end-begin):
            index = end-begin-i
            item = self.items[i+begin]
            p = 0
            if not place > floor(log10(item)):
                p = int(str(item)[place])
            index = offset[p]-1
            newItems[index] = item
            offset[p] = offset[p] + 1


