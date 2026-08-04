class Solution(object):
    def countSymmetricIntegers(self, low, high):
        def isSym(x):
            s=str(x)
            if len(s)%2!=0:
                return False
            n=len(s)//2
            return sum(map(int,s[:n]))==sum(map(int,s[n:]))
        cnt=0
        for i in range(low,high+1):
            if isSym(i):
                cnt+=1
        return cnt