from sort_function1 import *

def test_sort():
    print("Test #1")
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    passed = A == A_sorted
    print("Ok" if passed else "Fail")

    print("testcase #2: ", end="")
    A = []
    A_sorted = []
    sort_algorithm(A)
    passed = A == A_sorted
    print("Ok" if passed else "Fail")

    print("testcase #3: ", end="")
    A = [1, 2, 3, 4, 5]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    passed = A == A_sorted
    print("Ok" if passed else "Fail")
  
test_sort()
