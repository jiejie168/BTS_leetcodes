__author__ = 'Jie'

"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums, target: int):
        # use multiple binary search
        if nums is None:
            return [-1,-1]
        n=len(nums)

        left,right=0,n-1
        # first use binary search to find one target value in the sorted array.
        while left<=right:
            mid=(left+right)//2
            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            else:
                return [self.helper_left(nums,0,mid,target),self.helper_right(nums,mid,n-1,target)]

    def helper_left(self,nums,left,right,target):
        # use binary search to find the left most duplicate target
        while left<right:
            # noted that left should not be equal to right, otherwise there would be a out of boundary error
            mid=(left+right)//2
            if target>nums[mid]:
                left=mid+1
            elif target>nums[mid-1]:
                # the left most duplicate element is found
                return mid
            else:
                right=mid-1
        return left

    def helper_right(self,nums,left,right,target):
        # use binary search to find the right most duplicate target.
        while left<right:
            mid=(left+right)//2
            if target<nums[mid]:
                right=mid-1
            elif target<nums[mid+1]:
                return mid
            else:
                left=mid+1
        return right

solution=Solution()
nums=[5,7,7,8,8,10]
target=8
ans=solution.searchRange(nums,target)
print (ans)
