#String Reversal - example case, if input is abcde, output is edcba

def reverse(string):

    if len(string) == 1:
        return string
    
    else:
        return string[-1] + reverse(string[:-1])
    
#palindrome
#palindrome is a word where if you reverse the character order, you end up with the original word. ex kayak is palindrome

def ispalindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    
    elif string[0] != string[-1]:
        return False
    
    else:
        return ispalindrome(string[1:-1])
    
    
def fibo(n):
    if n==1 or n==2:
        return 1
    return fibo(n-1) + fibo(n-2)