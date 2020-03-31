import random

def bitonic_sort(up, x):
    """Bitonic sort.

    Args:
      up: ascending if ''up'' is true, and decreasing otherwise.
      x: A sequence of integers.

    Returns:
      Sorted sequence of integers.
    """
    if len(x) <= 1:
        return x
    else:
        first = bitonic_sort(True, x[:len(x) // 2])
        second = bitonic_sort(False, x[len(x) // 2:])
        return bitonic_merge(up, first + second)

def bitonic_merge(up, x):
    # Assume input x is bitonic, and sorted list is returned 
    if len(x) == 1:
        return x
    else:
        bitonic_compare(up, x)
        first = bitonic_merge(up, x[:len(x) // 2])
        second = bitonic_merge(up, x[len(x) // 2:])
        return first + second

def bitonic_compare(up, x):
    dist = len(x) // 2
    for i in range(dist):
        if (x[i] > x[i + dist]) == up:
            x[i], x[i + dist] = x[i + dist], x[i]  # Swap

def is_ordered(A):
    size = len(A)
    for i in range(size-1):
        if A[i] > A[i+1]:
            return False
    return True

def main():
    for list_size in range(4, 33):
        print("Lists of size {}".format(list_size))
        pos = 0
        neg = 0
        for i in range(1000):
            A = [random.randint(0, 100) for i in range(list_size)]
            A = bitonic_sort(True, A)
            if is_ordered(A):
                pos += 1
            else:
                neg += 1
        print("There were {} positive results".format(pos))
        print("There were {} negative results".format(neg))
        print("="*30+"\n")
if __name__ == '__main__':
    main()
