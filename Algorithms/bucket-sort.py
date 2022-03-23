#Bucket Sort
#Asume input is drawn from a uniform distribution
from random import uniform

def InsertionSort(A):
    for i in range(1, len(A)):
        current = A[i] #store the i-th iteration element 
        j = i-1 #compare it with its previous neighbour
        while j >= 0 and A[j] > current:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = current #smallest number is in sorted

def BucketSort(A):
    n = len(A)
    b = [[] for i in range(n)]
    sort_list = []
    
    for i in range(n):
        k = int(n*A[i])
        b[k].append(A[i])
        
    for j in b:
        InsertionSort(j)
        sort_list += j
    return sort_list
    
h = [round(uniform(0,1), 3) for i in range(10)]
print(h)
sort_h = BucketSort(h)
print(sort_h)