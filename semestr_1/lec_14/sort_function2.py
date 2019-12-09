def sort_algorithm(A):
    """
    Sorting of list on place. Using Bubble Sort algorithm.
    """
    N = len(A)
    for i in range(N-1):
        for k in range(N-1):
            if A[k] >= A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
