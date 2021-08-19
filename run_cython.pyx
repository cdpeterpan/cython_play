cpdef int test(int x):
    cdef int y = 1
    cdef int i
    for i in range(x+1):
        y *= i
    return y
