class Solution:
    def sumBase(self,n,k):
        s=0
        while n>0:
            s+=n%k
            n//=k
        return s