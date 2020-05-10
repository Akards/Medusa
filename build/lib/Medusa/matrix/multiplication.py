import numpy as np
import multiprocessing as mp
from functools import partial

def multiply(A, B, proc_num):
    """
    Multiplies 2D numpy matrices A and B using n total processes.
    Args:
        A (np.array): a 2D matrix
        B (np.array): a 2D matrix
        proc_num (int): number of processors
    Returns:
        The product of A*B
    """
    if A.ndim != 2:
        raise Exception("Must provide 2-dimensional matrix. Matrix A has {} dimensions".format(A.ndim))
    if B.ndim != 2:
        raise Exception("Must provide 2-dimensional matrix. Matrix B has {} dimensions".format(B.ndim))

    if A.shape[1] != B.shape[0]:
        raise Exception("A ({}x{}) and B ({}x{}) row number does not match column number".format(A.shape[1], A.shape[0], B.shape[1], B.shape[0]))

    # Create a manager, and give it a zeroed list with the size of the result
    manager = mp.Manager()
    C = manager.list([0 for n in range(A.shape[0]*B.shape[1])])

    # Add all slice indices for Multiprocessing to map later
    slices = [row_num for row_num in range(A.shape[0])]
    if proc_num > len(slices):
        proc_num = len(slices)

    B_t = np.transpose(B) # Transpose for row-major order traversal
    pool = mp.Pool(proc_num)
    mult = partial(multiply_row, A, B_t, C)
    pool.map_async(mult, slices)
    pool.close()
    pool.join()
    C = np.array(C).reshape(A.shape[0], B.shape[1])
    return C

def multiply_row(A, B, C, row):
    for j in range(B.shape[0]):
        C[row*B.shape[0] + j] += np.dot(A[row], B[j])

def main():
    A = np.array([[1, 2, 3, 4, 5] for i in range(5)])
    B = np.array([[i%2] for i in range(1, 6)])
    C = multiply(A, B, 5)
    print(C)

if __name__ == '__main__':
    main()
