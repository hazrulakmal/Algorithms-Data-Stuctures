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