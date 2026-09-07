class Solution(object):
    def distinctSubseqII(self, s):
        MOD=10**9+7
        dp=1
        last=[0]*26
        for c in s:
            x=ord(c)-ord('a')
            new=2*dp-last[x]
            last[x]=dp
            dp=new%MOD

        return (dp-1)%MOD