from random import shuffle  # it randomizes order of elements


def test_sort():
    print("Test sorting algorithm:")
    passed = True
    
    passed &= test_sort_works_in_simple_cases()
    passed &= test_sort_algorithm_stable()
    passed &= test_sort_algorithm_is_universal()
    passed &= test_sort_algorithm_scalability()
    
    print("Summary:", "Ok" if passed else "Fail")
    

def test_sort_works_in_simple_cases():
    print("- sort algorithm works in simple cases:", end=" ")
    passed = True
    
    for A1 in ([1], [], [1, 2], [1, 2, 3, 4, 5], 
               [4, 2, 5, 1, 3], [5, 4, 4, 5, 5],
               list(range(20)), list(range(20, 1, -1))):
        A2 = sorted(list(A1))  # yes, we are cheating here to shorten example
        sort_algorithm(A1)
        passed &= all(x == y for x, y in zip(A1, A2))
     
    print("Ok" if passed else "Fail")
    return passed


def test_sort_algorithm_stable():
    print("- sort algorithm is stable:", end=" ")
    passed = True
    
    for A1 in ([[100] for i in range(5)],
               [[1, 2], [1, 2], [2, 2], [2, 2], [2, 3], [2, 3]],
               [[5, 2] for i in range(30)] + [[10, 5] for i in range(30)]):
        shuffle(A1)
        A2 = sorted(list(A1))  # here we are cheating: standard sort is stable
        sort_algorithm(A1)
        # to test stability we will check A1[i] not equals A2[i], but is A2[i]
        passed &= all(x is y for x, y in zip(A1, A2))
     
    print("Ok" if passed else "Fail")
    return passed


def test_sort_algorithm_is_universal():
    print("- sort algorithm is universal:", end=" ")
    passed = True
    
    # testing types: str, float, list
    for A1 in (list('abcdefg'),
               [float(i)**0.5 for i in range(10)],
               [[1, 2], [2, 3], [3, 4], [3, 4, 5], [6, 7]]):
        shuffle(A1)
        A2 = sorted(list(A1))
        sort_algorithm(A1)
        passed &= all(x == y for x, y in zip(A1, A2))
     
    print("Ok" if passed else "Fail")
    return passed


def test_sort_algorithm_scalability(max_scale=100):
    print("- sort algorithm on scale={0}:".format(max_scale), end=" ")
    passed = True
    
    for A1 in (list(range(max_scale)),
               list(range(max_scale//2, max_scale)) + list(range(max_scale//2)),
               list(range(max_scale, 0, -1))):
        shuffle(A1)
        A2 = sorted(list(A1))
        sort_algorithm(A1)
        passed &= all(x == y for x, y in zip(A1, A2))
     
    print("Ok" if passed else "Fail")
    return passed


def sort_algorithm(A):
    "Sorting of list A on place."
    pass

 
test_sort()

