__author__ = 'Jie'
"""
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

solution=Solution()
nums=[4,5,6,7,0,1,2]
target=0
ans=solution.search(nums,target)
print (ans)