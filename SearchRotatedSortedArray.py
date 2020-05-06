__author__ = 'Jie'
"""
uppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""
class Solution:
    def search(self, nums, target: int) -> int:
        # cut directly from the center.
        # judge if left is ascending or the right is ascending.
        n=len(nums)
        left,right=0,n-1

        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            if target>=nums[0] :
                # search in the left, ascending array for the target
                if nums[mid]<target and nums[mid]>=nums[0]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                # search in the right array
                if  nums[mid]>=nums[0] or nums[mid]<target:
                    # two types of conditions
                    left=mid+1
                else:
                    right=mid-1
        return -1
    def search_1(self,nums, target):
        # a more clear binary search
        n=len(nums)
        left,right=0,n-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            # left halve is sorted, and search on the left half
            if nums[mid]>=nums[left]:
                #[2,4,5,6,7,0,1] -> left[2,4,5]+ mid[6]+ right[7,0,1]
                if target>nums[mid] or target<nums[left]:
                    # since left half is sorted, nums[mid] is the largest element in the left part. if target is larger
                    # than this largest element, or the target is smaller than the minimum element, it means that the search
                    # is now goint to the right part. Hence, left move forward.
                    left=mid+1
                else:
                    right=right-1
            else:
                # right half is sorted, and search on the right half
                # [5,6,7,0,1,2,4] -> left[5,6,7]+ mid+ right[1,2,4]
                if target< nums[mid] or target > nums[right]:
                    right=mid-1
                else:
                    left=mid+1
        return -1

solution=Solution()
nums=[4,5,6,7,0,1,2]
target=0
ans=solution.search(nums,target)
print (ans)