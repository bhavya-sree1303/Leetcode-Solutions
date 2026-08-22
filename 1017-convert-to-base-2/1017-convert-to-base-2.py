class Solution:
    def baseNeg2(self, n):
        if n==0:
            return "0"
        ans=""
        while n:
            r=n%-2
            n//= -2
            if r<0:
                r+=2
                n+=1
            ans=str(r)+ans

        return ans