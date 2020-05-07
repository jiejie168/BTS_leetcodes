__author__ = 'Jie'
"""

"""
class Solution:
    def twoSum(self, nums, target: int):
        # use hash table. O(n)
        hash_new={}
        for i,elem in enumerate (numbers):
            temp=target-elem
            if temp not in hash_new:
                hash_new[elem]=i
            else:
                return [hash_new[temp]+1,i+1]
    def twoSum_1(self,nums,target):
        # use two-pointers
        n=len(nums)
        left,right=0,n-1
        sums=0 # the sum of two elements
        while left<right:
            sums=nums[left]+nums[right]
            # right pointer moves to left, if sums is too big
            if sums>target:
                right-=1
            elif sums<target:
                left+=1
            else:
                return [left+1,right+1]

solution=Solution()
numbers=[2,7,11,15]
target=9
ans=solution.twoSum_1(numbers,target)
print (ans)