#Q1
#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
#"a" = 1, "b" = 2, etc.

def alphabet_position(text):
    text = ''.join(e for e in text if e.isalnum()) #remove non-alphabets and non-numbers
    text = text.lower()
    if len(text) == 0:
        return ""
    else:    
        return find(text, 0)
    
def find(text, index):
    #store letter numbers in dic for fast retrival O(n)
    stor = {"a":1,"b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20,"u":21, "v":22,"w":23,"x":24,"y":25, "z":26}
    if index == len(text)-1:
        return str(stor[text[-1]])
    else:
        ch = text[index]
        return str(stor[ch]) + " " + find(text, index+1)
    
def alphabet_position_1(text): #clever solution
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


#Q2
#A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
#For example, take 153 (3 digits), which is narcisstic:
#1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
def narcissistic( value ):
    # Code away
    total = 0
    for i in str(value): #so that we can reiterate on each digit
        total += int(i)**len(str(value))
    return total == value