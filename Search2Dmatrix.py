__author__ = 'Jie'
"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # binary search
        if matrix is None:
            return False
        if matrix==[] or matrix==[[]]:
            return False
        m=len(matrix)
        n=len(matrix[0])
        flattened=[elem for row in matrix for elem in row]

        left, right=0,m*n-1
        while left <=right:
            mid=(left+right)//2
            if flattened[mid]==target:
                return True
            elif flattened[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False

solution=Solution()
matrix=[[1]]
target=2
ans=solution.searchMatrix(matrix,target)
print (ans)


