#Randomised Quicksort 
#Expected running time is O(nlogn)

from random import randint

def RandomisedPartition(A, p, r):
    pivot = randint(p, r)
    A[pivot], A[r] = A[r], A[pivot]
    return Partition(A, p, r)

def Partition(A, p, r):
    x = A[r]
    i = p-1
    
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def RandomisedQuicksort(A, p, r):
    if p < r:    
        q = RandomisedPartition(A, p, r)
        RandomisedQuicksort(A, p, q-1)
        RandomisedQuicksort(A, q+1, r)