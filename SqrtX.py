__author__ = 'Jie'
"""
69. Sqrt(x)

Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
class Solution:
    def mySqrt(self, a: int) -> int:
        # naive method
        # search every number
        if a<=1:
            return a
        if a==2:
            return 1
        for i in range(2,a):
            if i*i>a:
                return i-1

    def mySqrt_1(self,a):
        # utlize binary search. O(loga)
        left=1
        right=a
        while left<=right:
            mid=left+(right-left)//2  # the start point is 1.
            if mid>a/mid:
                right=mid-1
            else:
                left=mid+1
        return right

    def mySqrt_2(self,a):
        #NewtonMethod
        # X_(n+1)=X_n-f(X_n)/f'(X_n)
        # F(X)=X^2-a
        resid=1e-3
        x0=a
        while x0*x0-a>resid:
            x0=(x0+a//x0)//2 # the iterative equation
        return x0

solution=Solution()
a=5
ans=solution.mySqrt_2(a)
print (ans)



