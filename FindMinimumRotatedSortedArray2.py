__author__ = 'Jie'
"""
154. Find Minimum in Rotated Sorted Array II
Hard

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
"""
class Solution:
    def findMin(self, nums) -> int:
        # there is a little confused for me for this problem
        # divide and conquer idea. It is similar to the peak finding problems.
        n=len(nums)
        if nums[0]<nums[n-1]:
            return nums[0]
        left,right=0,n-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                # means that the minimum is in the left rotated part
                left=mid+1
            elif nums[mid]<nums[left]:
                right=mid
            else:
                right-=1
        return nums[left]


    def findMin_2(self,nums):
        # use recursive search; divide and conquer.
        return self.find_helper(nums,0,len(nums)-1)

    def find_helper(self,nums,left,right):
        # recursive method
        # the first terminate condition: only two element left in an array, compared the two elements
        if left+1>=right:
            return min(nums[left],nums[right])
        if nums[left]<nums[right]:
            # sorted array, so the minimum is the left one.
            return nums[left]
        mid=left+(right-left)//2
        # recursive search in the left part and the right part, then obtain the minimum value.
        return min(self.find_helper(nums,left,mid-1),self.find_helper(nums,mid,right))


solution=Solution()
nums=[2,2,2,2,2,2,3,1,2]
ans=solution.findMin_2(nums)
print (ans)