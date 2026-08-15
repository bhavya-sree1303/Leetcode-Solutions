class Solution(object):
    def closestDivisors(self, num):
        for x in [num + 1, num + 2]:
            i = int(x ** 0.5)
            while i>0:
                if x%i==0:
                    a=i
                    b=x//i
                    if x==num+1:
                        ans=[a, b]
                        diff=b-a
                    elif b-a<diff:
                        ans=[a, b]
                    break
                i-=1
        return ans