__author__ = 'Jie'
"""
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
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