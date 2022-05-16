#Fibo in linear time

def linear_fibo(n):
    if n==1 or n==2:
        return 1
    a = 1
    b = 1
    for i in range(n-2):
        new = a + b
        a = b
        b = new
    return b
