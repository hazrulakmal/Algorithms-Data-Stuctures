# recursive algorithms
# pemutation code

def pemute(n):
    # input has to be intergers
    # big o(n) running time
    if n == 1:
        return 1
    
    else:
        return n*pemute(n-1)
    
def pemute_iterative(n):
    # iterative algorithm for pemutation
    i = 1
    while n > 1:
        i *= n
        n -= 1
        
    return i  

#colazt conjecture. We can go back 1 from any positive integers if we do following opearation multiple times 1. 2/n for even and 3n+ 1 for odd

def collaz_iterative(n):
    # iterative
    j = 0
    while n > 1 :
        if  n%2 == 0:
            n = n/2
            j += 1
        else:
            n = 3*n + 1
            j += 1
    return j

def collaz(n):
    
    if n==1:
        return 0
    
    elif n%2 ==0:
        return 1 + collaz(n/2)
    
    else:
        return 1 + collaz(3*n +1)
    
