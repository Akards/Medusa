import numpy as np
import multiprocessing as mp
from functools import partial

"""
//computes A * B = C. Loop order: i, k, j
void mxm_ikj(double *A, double *B, double *C, int size) {
    int i, j, k, ii;
    #pragma omp parallel for private(j, k)
    for(i = 0; i < size; i++) {
        ii = i * size;
        for(k = 0; k < size; k++) {
            for(j = 0; j < size; j++) {
                C[ii+j] += A[ii+k]*B[k*size+j];
            }
        }
    }
    return;
}
"""
def multiply(A, B, proc_num):
    """
    Multiplies 2D numpy matrices A and B using n total processes.
    Args:
        A (np.array): a 2D matrix
        B (np.array): a 2D matrix
        n (int)     : number of processors
    Returns:
        The product of A*B
    """
    if A.ndim != 2:
        raise Exception("Must provide 2-dimensional matrix. Matrix A has {} dimensions".format(A.ndim))
    if B.ndim != 2:
        raise Exception("Must provide 2-dimensional matrix. Matrix B has {} dimensions".format(B.ndim))

    proc_arr = []

    # Do not allow for there to be more processors than the minimum dimension
    # of matrix
    smallest_dimension = min([A.shape[0], A.shape[1], B.shape[0], B.shape[1]])
    if proc_num > smallest_dimension:
        proc_num = smallest_dimension

    # Create a manager, and give it a zeroed list with the size of the result
    manager = mp.Manager()
    C = manager.list([0 for n in range(A.shape[0]*B.shape[1])])

    # Add all slice indices for Multiprocessing to map later
    slices = [row_num for row_num in range(A.shape[0])]
    """
    slice_a_col = A.shape[0] // proc_num
    slice_b_col = B.shape[0] // proc_num
    slice_a_row = A.shape[1] // proc_num
    slice_b_row = B.shape[1] // proc_num
    """

    B_t = np.transpose(B) # Transpose for row-major order traversal
    pool = mp.Pool(proc_num)
    mult = partial(multiply_row, A, B_t, C)
    pool.map_async(mult, slices)
    pool.close()
    pool.join()
    C = np.array(C).reshape(A.shape[0], B.shape[1])
    return C

    """
    # Spawn all processors demanded
    for i in range(proc_num):
        # Calculate the indices of a matrix slice
        min_a_row = i*slice_a_row
        max_a_row = i*(slice_a_row+1)
        min_b_row = i*slice_b_row
    artial(multiply_row, A, B_t, C)ssert(A @ B, C)
        max_b_row = i*(slice_b_row+1)
        # Last processor might not get as big of a slice
        if i == proc_num - 1:
            max_a_row = A.shape[0]
            max_b_row = B_t.shape[0]

        min_a_col = A
        p = mp.process(target=compute_partial_sum,
                       args=(A, B_t, C))
    """
def multiply_row(A, B, C, row):
    for j in range(B.shape[0]):
        C[row*A.shape[0] + j] += np.dot(A[row], B[j])

def main():
    A = np.arange(16).reshape((4, 4))
    B = np.arange(16).reshape((4, 4))
    print("This is A")
    print(A)
    print("This is B")
    print(B)
    print("C = A*B")
    C = multiply(A, B, 4)
    print(A @ B)
    print(C)

if __name__ == '__main__':
    main()
