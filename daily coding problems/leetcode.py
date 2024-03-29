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


# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def search_palindrome(left, right):
            while left >= 0 and right < len(s) and s[right] == s[left]:
                left -= 1
                right += 1
            return s[left+1:right]

        result = ""

        if len(s) < 2 or s[::-1] == s:
            return s

        for i in range(len(s)-1):
            palindrome_sub_even = search_palindrome(i, i+1)
            palindrome_sub_odd = search_palindrome(i, i+2)
            result = max(result, palindrome_sub_even, palindrome_sub_odd, key=len)

        return result
    
# 9. Palindrome Number
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            x = str(x)
            return x == x[::-1]

class Solution:
    def isPalindrome(self, x: int) -> bool:

        def recursive_palindrome(word):
            if len(word) < 2: return True
            if word[0] != word[-1]: return False
            return recursive_palindrome(word[1:-1])

        word = str(x)
        return recursive_palindrome(word)

#234. Palindrome Linked List
#Given the head of a singly linked list, return true if it is a palindrome.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        number_string = ""

        cur = head
        while cur:
            number = cur.val
            number_string += str(number)
            cur = cur.next

        if number_string == number_string[::-1] : 
            return True
        else:
            return False


#94. Binary Tree Inorder Traversal
#Given the root of a binary tree, return the inorder traversal of its nodes' values.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # If root is None then return an empty array
        if root is None:
            return []
        else:
            # Recurse on the left subtree, then the root node, then the right subtree
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
#206. Reverse Linked List
#Given the head of a singly linked list, reverse the list, and return the reversed list.
#Recursive solution

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            # If the list is empty or has only one node, no change is needed, so just return the original head.
            return head
        else:
            # Reverse the sublist whose head is head.next
            new_head = self.reverseList(head.next)
            # head.next is the tail of the reversed sublist. Point the tail to head, forming the original sublist.
            head.next.next = head
            # Set the next of head to None, breaking the link of the original sublist.
            head.next = None
            # Return the new head of the reversed sublist.
            return new_head
        
#iterative solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

#100. Same Tree
#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are empty, they are the same
        if p is None and q is None:
            return True
        # If one of the trees is empty, they are not the same
        elif p is None or q is None:
            return False
        # If the values of the roots are the same, check if the left and right subtrees are the same
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If the values of the roots are not the same, the trees are not the same
        else:
            return False

#104. Maximum Depth of Binary Tree
#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
