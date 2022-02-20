# decimal to binary. Concatenate the remiander to the binary code 

def remainder(n, result):
    # n must be integers but formatted in string, result variable for first recursion should be an empty string. 
    if n == 0:
        return result
    
    result = str(n%2) + result
    return remainder(n//2, result)
    

# merge sort 

def mergesort(array):
    
    if len(array) <= 1:
        return array
    
    mid = len(array)//2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
        
    return merge(left, right)

def merge(left, right):
    l = 0
    r = 0
    ordered = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            ordered.append(left[l])
            l += 1
        else:
            ordered.append(right[r])
            r += 1
            
    ordered += left[l:]
    ordered += right[r:]
    return ordered
    
            
        