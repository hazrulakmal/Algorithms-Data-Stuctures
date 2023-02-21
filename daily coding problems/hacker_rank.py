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
        if string[i] in vowels: #if the letter in the string is a vowel
            kevin_score += (len(string) - i) #add the score to kevin's score
        else: #if the letter in the string is not a vowel
            stuart_score += (len(string) - i) #add the score to stuart's score
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
        
        # Dictionary to store the value and its index
        d = {}
        for i, j in enumerate(nums):
            # Calculate the remaining value
            r = target - j
            # If the remaining value is in the dictionary, then return the index of the remaining value and the current index
            if r in d: return [d[r], i]
            # If the remaining value is not in the dictionary, then add the current value and index into the dictionary
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
        dummy = ListNode(0) #create a dummy node to return
        cur = dummy #set cursor to dummy
        extra_val = 0 #set extra value to 0
        
        while l1 or l2 or extra_val: #while one of the linked lists or extra value is non-zero
            l1val = l1.val if l1 else 0 #set l1val to 0 if l1 is None else l1.val
            l2val = l2.val if l2 else 0 #set l2val to 0 if l2 is None else l2.val

            #computation
            v = l1val + l2val + extra_val #add l1val, l2val, and extra_val
            extra_val = v // 10 #set extra_val to v // 10
            final_v = v % 10 #set final_v to v % 10
            cur.next = ListNode(final_v) #set cursor.next to a new ListNode with value final_v

            #update cursor
            cur = cur.next #set cursor to cursor.next
            l1 = l1.next if l1 else None #set l1 to l1.next if l1 is not None else None
            l2 = l2.next if l2 else None #set l2 to l2.next if l2 is not None else None

        return dummy.next #return dummy.next
    
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

#30 days of code

# Day 2: Operators
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
# Round the result to the nearest integer.

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tips = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    print(round(meal_cost + tips + tax)) 

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)

# Day 8: Dictionaries and Maps
# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query your phone book for.
# For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for name is not found, print Not found instead.
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

contact_details = dict()
for i in range(n):
    name_num = input().split()
    name = name_num[0]
    num = name_num[1]
    contact_details[name] = num
    

while True:
    try:
        name_to_query = str(input())
        if name_to_query in contact_details:
            print(f'{name_to_query}={contact_details[name_to_query]}')
        else:
            print( "Not found")
    except EOFError:
        break        


#Day 10: Binary Numbers
# Given a base-10 integer, n, convert it to binary (base-2).
# Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

import math
import os
import random
import re
import sys

def maxConsecutiveOnes(n):
    # Write your code here
    binary = bin(n)[2:]
    max_ones = 0
    count = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            count += 1
        else:
            count = 0
        max_ones = max(max_ones, count)
    return 

#Day 11: 2D Arrays
# Given a 6x6 2D Array, arr:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in arr's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values.
# Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    # Write your code here
    max_sum = -63 # setting max sum to -63
    for i in range(4): # iterating over the first four rows
        for j in range(4): # iterating over the first four columns
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] # adding all the values in the hourglass
            max_sum = max(max_sum, sum) # updating maximum sum if required
    return max_sum

