__author__ = 'Jie'
"""
153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""
## idea:  binary search.  c1:[4,5,6,7,0,1,2] ->  0 is less than mid:7, any other following element
# is larger than the former one -> 0 is the minimum -> the search idea
# array rules:  increase+ Max+min+increase.
class Solution:
    def findMin(self, nums) -> int:
        n=len(nums)
        if nums[0]<nums[n-1]:
            return nums[0]

        left,right=0,n-1
        while left <right:
            # no equal, since there is no need to loop every element
            mid=(left+right)//2
            if nums[mid] <nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]> nums[left]:
                left=mid+1
            else:
                right=mid-1
        # when the nums has only one element, then return
        return nums[left]

solution=Solution()
# nums=[4,5,6,7,0,1,2]
nums=[1]
ans=solution.findMin(nums)
print (ans)