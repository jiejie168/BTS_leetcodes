__author__ = 'Jie'
# coding: utf-8
"""
162. Find Peak Element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:
Your solution should be in logarithmic complexity.
"""
class Solution:
    def findPeakElement(self, nums) -> int:
        # linear comparison, O(n)
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                return i
        return n-1

    def findPeakElement_1(self,nums):
        # recursive binary search
        # since the array is not sorted, the binary search should be updated.
        # the terminate condition: if left=right-> return left
        n=len(nums)
        return self.helper_rec(nums,0,n-1)

    def helper_rec(self,nums,left,right):
        # recursive binary search
        # since the array is not sorted, the binary search should be updated.
        # the terminate condition: if left=right-> return left
        if left ==right:
            return left
        mid=(left+right)//2
        if nums[mid]< nums[mid+1]:
            return self.helper_rec(nums,mid+1,right)
        else:
            return self.helper_rec(nums,left,mid)

    def findPeakElement_2(self,nums):
        # divide and conquer, iterative for peaking problems
        n=len(nums)
        left,right=0,n-1
        # left can be not equal to right, since there must have a peak value according to the definition.
        while left<right:
            mid=(left+right)//2
            if nums[mid]> nums[mid+1]:
                # the mid could be the element we want to find.
                right=mid
            else:
                left=mid+1
        return left

solution=Solution()
nums=[1,2,1,3,5,6,4]
ans=solution.findPeakElement_1(nums)
print (ans)