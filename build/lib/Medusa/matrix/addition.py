import numpy as np
import multiprocessing as mp
from functools import partial

def add(A, B, proc_num):
    """
    Returns added matrices A and B
    Args:
        A (np.array): a 2D matrix
        B (np.array): another 2D matrix
        proc_num (int): number of processors
    Returns:
        The sum of A + B
    """
    # Checking if 2D and for congruency
    if A.ndim != 2:
        raise Exception("Must provide 2-dimensional matrix. Matrix A has {} dimensions".format(A.ndim))
    if B.ndim != 2:
        raise Exception("Must provide 2-dimensional matrix. Matrix B has {} dimensions".format(B.ndim))
    if A.shape[0] != B.shape[0] or A.shape[1] != B.shape[1]:
        raise Exception("Must provide 2-dimensional matrices with equivalent number of rows and columns")

    # Create a manager, and give it a zeroed list of size rows*cols
    manager = mp.Manager()
    C = manager.list([0 for n in range(A.shape[0]*A.shape[1])])

    # Linearize matrices
    a = A.flatten()
    b = B.flatten()

    # Add all slice indices for Multiprocessing to map later
    slices = [i for i in range(A.shape[0]*A.shape[1])]

    add = partial(add_value, a, b, C)
    pool = mp.Pool(proc_num)
    pool.map_async(add, slices)
    pool.close()
    pool.join()

    # Convert linearized sum of A and B into 2D array in shape rows*cols
    C = np.array(C).reshape(A.shape[0], A.shape[1])
    return C

def add_value(A, B, C, idx):
    print("This is called?")
    print("{} + {}".format(A[idx], B[idx]))
    C[idx] = A[idx] + B[idx]
