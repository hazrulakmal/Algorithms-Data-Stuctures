#Dynamic Arrays in Python
#Double-Halving concept in expanding/shrinking an array
#amotized cost is constant if new element is added at the end of the list
#amotized cost is linear if new element is added at the front of a list

#When the expensive cost happens, it wont happen again after a while so the cost is amotized
from time import time

def slowArray(n):
    array = []
    for i in range(n):
        array.insert(0, i)

def fastArray(n):
    array = []
    for i in range(n):
        array.insert(i, i)
        
t1 = time()
slowArray(100000)
t2 = time()
fastArray(100000)
t3 = time()   

print(f"slow array time is {round(t2-t1,6)}.")     
print(f"fast array time is {round(t3-t2,6)}.")  