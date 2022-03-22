#Quick Sort

def Partition(A, p, r):
    # i is the number of available space for element less than the pivot
    x = A[r] #pivot(last element)
    i = p-1 #before iteration, no comparision made so no number is know to be less than the pivot
    
    for j in range(p, r): #expanding the search
        if A[j] <= x:
            i = i + 1 #increase one space to accomodate A[j] element that is smaller than the pivot
            A[i], A[j] = A[j], A[i] #swab j element that is bigger than the pivot with i element that is smaller than the pivot
    A[i+1], A[r] = A[r], A[i+1] #arrange the pivot to its ordered place
    return i + 1
        
    
def QuickSort(A, p, r): #recursive function
    if p < r : #baseline to stop the recursive loop.
        q = Partition(A, p, r)
        QuickSort(A, p, q-1) #arrange the reimining unordered elements in the left side of the pivot
        QuickSort(A, q+1, r) #does the same thing as above but on the right side of the pivot
    

    