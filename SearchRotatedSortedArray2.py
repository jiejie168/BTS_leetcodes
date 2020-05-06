__author__ = 'Jie'
"""
81. Search in Rotated Sorted Array II
Medium
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""

class Solution:
    def search(self, nums, target: int) -> bool:
        # updated binary search,
        # either left halve is sorted, or the right half is sorted.
        # hence, search always ont the sorted half
        n=len(nums)
        left,right=0,n-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            # judge if the left half is sorted
            # the second "or" indicates the right is not sorted in case duplicated elements are presented.
            if nums[mid]>nums[left] or nums[mid]>nums[right]:
                if nums[mid]< target or target<nums[left]:
                    # since left half is sorted, nums[mid] is the largest element in the left part. if target is larger
                    # than this largest element, or the target is smaller than the minimum element, it means that the search
                    # is now goint to the right part. Hence, left move forward.
                    left=mid+1
                else:
                    right=right-1

            #judge if the right half is sorted, then sorted within this part.
            elif nums[mid]<nums[left] or nums[mid]<nums[right]:
                if target<nums[mid]  or target>nums[right]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                # the case all elements are duplicated
                #[3,3,3,3,3,3,3]
                right-=1

        return False
solution=Solution()
nums = [2,5,6,0,0,1,2]
target = 0
ans=solution.search(nums, target)
print (ans)


