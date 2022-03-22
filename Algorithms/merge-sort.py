# Merge sort Recap

def merge_sort(a):
    
    if len(a) <= 1:
        return a
    
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    
    return merge(left, right)

def merge(left, right):
    sort = []
    l = 0
    r = 0
    
    while len(left) > l and len(right) > r:
        if left[l] <= right[r]:
            sort.append(left[l])
            l += 1
        else:
            sort.append(right[r])
            r += 1
            
    sort += left[l:]
    sort += right[r:]
    
    return sort


