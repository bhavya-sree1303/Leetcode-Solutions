class Solution:
    def stoneGameIII(self, stoneValue):
        n=len(stoneValue)
        a=b=c=0
        for i in range(n-1,-1,-1):
            take1=stoneValue[i]-a
            take2=stoneValue[i]+(stoneValue[i+1] if i+1<n else 0)-b
            take3=stoneValue[i]+(stoneValue[i+1] if i+1<n else 0)+(stoneValue[i+2] if i+2<n else 0)-c
            cur=max(take1,take2,take3)
            a,b,c=cur,a,b
        if a>0:return "Alice"
        if a<0:return "Bob"
        return "Tie"