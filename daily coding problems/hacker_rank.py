# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following: 123...n
# Note that "..." represents the consecutive values in between.
# Example
# n = 5
# Print the string 12345.
# Input Format
# The first line contains an integer .

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')


# kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Your task is to determine the winner of the game and their score.

def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += (len(string) - i)
        else:
            stuart_score += (len(string) - i)
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


#factorial recursive funtion given input n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#two sum problem given array of integers and target sum
#algorithm less than O(n^2) time complexity
#algorithm O(n) space & time complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i

#2. Add Two Numbers
#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in reverse order and each of their nodes contain a single digit.
#Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        extra_val = 0
        
        while l1 or l2 or extra_val:
            l1val = l1.val if l1 else 0 #incase if one linked list is shorter than the other
            l2val = l2.val if l2 else 0

            #computation
            v = l1val + l2val + extra_val
            extra_val = v // 10
            final_v = v % 10
            cur.next = ListNode(final_v)

            #update cursor
            cur = cur.next
            l1 = l1.next if l1 else None #also handles llinked list length 
            l2 = l2.next if l2 else None

        return dummy.next
    
# Merger two sorted linked lists
# Given two sorted linked lists, merge them together in ascending order and return a reference to the merged list.
# A linked list is a linear data structure where each element is a separate object.
# Each node in a list consists of two items - the data and a reference to the next node.
# The last node has a reference to null. The entry point into a linked list is called the head of the list.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node to point to the head of the merged list
        # We will return the next node of the dummy node
        dummy = ListNode()
        cur = dummy

        # While both lists are not empty
        while list1 and list2:
            # If the value of the first node of list1 is less than or equal to the value of the first node of list2
            if list1.val <= list2.val:
                # Connect the node at the head of list1 to the merged list
                # Move the head of list1 to the next node
                cur.next = list1
                list1, cur = list1.next, cur.next
            else:
                # Connect the node at the head of list2 to the merged list
                # Move the head of list2 to the next node
                cur.next = list2
                list2, cur = list2.next, cur.next

        # If list1 is not empty, connect the rest of list1 to the merged list
        # If list2 is not empty, connect the rest of list2 to the merged list
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        # Return the head of the merged list
        return dummy.next



            