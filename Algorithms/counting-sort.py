#Counting sort
#Sorting in linear time O(n)
#Assume unordered list with non-negative integers.
#we know the max value.

def CountingSort(A, B, k):
    #k takes the maximum value in the list
    C = [0 for i in range(0, k+1)] #create freq table
    for j in range(len(A)): #cal the freq of each number
        C[A[j]] = C[A[j]]+ 1
    for i in range(1,k+1): #cumulutive sum
        C[i] = C[i] + C[i-1]
    for l in range(len(A)-1,-1,-1): #backward reiterate on A and put it in B at its right position 
        B[C[A[l]]-1] = A[l]
        C[A[l]] = C[A[l]]- 1
    return B
   
a = [1,2,3,3,6,1,8,3,5,6]        
k = max(a)
b = [0 for i in range(len(a))]

B= CountingSort(a, b, k)