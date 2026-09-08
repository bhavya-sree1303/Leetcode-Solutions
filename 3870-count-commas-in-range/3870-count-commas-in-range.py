class Solution:
    def countCommas(self,n):
        ans=0
        if n>=1000:
            ans+=n-999
        return ans