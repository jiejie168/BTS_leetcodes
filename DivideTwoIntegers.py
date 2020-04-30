__author__ = 'Jie'

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # only substraction can be used
        # bit manipulation method is used.
        # m<<1:m left move of one bit, equal to 2 times.
        flag=-1 if (dividend >0 and divisor <0) or (dividend <0 and divisor >0) else 1
        q=0
        dividend,divisor=abs(dividend),abs(divisor)
        time=0  # used for acceleration of q.
        # q is actually the final quotient
        while dividend>=divisor:
            tmp=dividend-(divisor<<time)
            if tmp>=0:
                q+=(1<<time)
                time+=1
                dividend=tmp
            else:
                # in case tmp <0, the step time decreases a little bit
                time-=1
        return max(min(q*flag,2**31-1),-2**31)

solution=Solution()
dividend=10
divisor=3
ans=solution.divide(dividend,divisor)
print (ans)
