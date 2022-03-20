#codewars decode morse code
#MORSE_CODE is pre-built library from codewars. if one wants to replicate this code, one must create a dictionary of the morse code first.
 
#In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
#The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

def decode_morse(morse_code):
    sentence = ""
    words = morse_code.lstrip().split("   ") #remove front whitespace and three whitespaces
    for word in words:
        for letter in word.split():
            sentence += MORSE_CODE[str(letter)] 
        sentence += " "
    return sentence[:-1] #exclude whitespace at the back
