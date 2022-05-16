#iterative binary search 

def binary_search(A, x):
    i, j = 0, len(A)-1
    while j>i:
        m = (i+j)//2
        if A[m] == x:
            return m
        elif A[m] > x:
            j = m-1
        else:
            i = m+1
    return print("not in the list bro")

b = [1,2,3,4,5,6,7,8,9,10]

def recursive_binary_search(A, x, i, j):
    m = (i + j)//2
    
    if j < i:
        return None
    elif A[m] > x:
        return recursive_binary_search(A, x, i, m-1)
    elif A[m] == x:
        return m
    else:
        return recursive_binary_search(A, x, m+1, j)