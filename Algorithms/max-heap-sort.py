#Heap sort using heap data structure

def swap(A, i, v):
    A[i], A[v] = A[v], A[i]
    return A

#Max-Heap 
def MaxHeapify(A, i, size):
    largest = i #access root index
    l =  2*i + 1 #acess left child index
    r = 2*i + 2 #access right child index
    
    for c in [l, r]:
        if c < size and A[c] >  A[largest]: #make sure index exists given the length of the array and compare child and root nodes
            largest = c
    if largest == i: #baseline to stop recursive call, the largest value is in the root node
        return
    swap(A, i, largest)
    MaxHeapify(A, largest, size)

def BuildMaxHeap(A):
    i = len(A)//2 - 1
    size = len(A)
    while i >= 0: 
        MaxHeapify(A, i, size)
        i -= 1 #be mindful of infinite loop.

#sort elements in increasing order
def HeapSort(A): 
    BuildMaxHeap(A) #build max heap tree from scratch
    size = len(A)
    while size > 1:
        swap(A, 0, size-1) #put the largest number in the "right" order that is at the end of the list.
        size -= 1
        MaxHeapify(A, 0, size)


 #Min-Heap
def MinHeapify(A, i, size):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    
    for c in [l,r]:
        if c < size and A[c] < A[smallest]:
            smallest = c
    
    if smallest == i: #if not means more swapping down the tree is needed
        return
    
    swap(A, i, smallest)
    MinHeapify(A, smallest, size)
    

def BuildMinHeap(A):
    i = len(A)//2 - 1
    size = len(A)
    while i >= 0: 
        MinHeapify(A, i, size)
        i -= 1

#sort element in decreasing order
def MinHeapSort(A):
    BuildMinHeap(A)
    size = len(A)
    while size > 0:
        swap(A, 0, size-1)
        size -= 1
        MinHeapify(A, 0, size)
         
        
h = [1,5,2,6,3,8,9]    

        
