#Next Permutation
#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
#The replacement must be in place and use only constant extra memory.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        # find the first decreasing number from the right
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        # if found, swap it with the number that is just larger than it
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # reverse the list after the number that is just larger than the first decreasing number
        reverse(nums, i + 1)

#decode string
#Given an encoded string, return its decoded string.
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

class Solution:
    def decodeString(self, s: str) -> str:
        """
        :type s: str
        Utilising a stack to store the current number and string to be repeated
        curNum: current number saves the number before the '[' which will be used to repeat the string when ']' is encountered 
        curString saves the string before the '[' which will be used to repeat the string when ']' is encountered
        CurNum*10 + int(char) is used to handle the case where the number is more than 1 digit
        """
        
        curNum = 0
        curString = ""
        stack = []

        for char in s:
            if char.isdigit():
                curNum = curNum*10 + int(char)
            elif char == "[":
                stack.append((curNum, curString))
                curNum = 0
                curString = ""
            elif char == "]":
                previous_num, previous_string = stack.pop()
                curString = previous_string + curString * previous_num
            else:
                curString += char

        return curString

#almost sorted
#Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.
#Swap two elements.
#Reverse one sub-segment.
#Determine whether one, both or neither of the operations will complete the task. If both work, choose swap. For instance, given the array  we see that swapping  and  satisfies our condition. For another array,  either swap  and  or reverse the segment  satisfy the conditions. Choose swap.


def almostSorted(arr):
    to_sort = arr.copy()
    # If the array is already sorted, print yes and return
    if arr == sorted(arr):
        print('yes')
        return
    # Find the first number that is out of order
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            break
    # Find the last number that is out of order
    for j in range(len(arr)-1, 0, -1):
        if arr[j] < arr[j-1]:
            break
    # Swap the first and last numbers that are out of order
    to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
    # If the array is now sorted, print yes and swap
    if to_sort == sorted(arr):
        print('yes')
        print('swap', i+1, j+1)
    # If the array is not sorted, reverse the out of order numbers
    else:
        arr[i:j+1] = arr[i:j+1][::-1]
        # If the array is now sorted, print yes and reverse
        if arr == sorted(arr):
            print('yes')
            print('reverse', i+1, j+1)
        # If the array is still not sorted, print no
        else:
            print('no')












