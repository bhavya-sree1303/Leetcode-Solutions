class Solution:
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        def cost(seq):
            cur=startAt
            c=0
            for ch in seq:
                d=int(ch)
                if cur!=d:
                    c+=moveCost
                c+=pushCost
                cur=d
            return c
        
        ans=float('inf')
        
        for m in range(100):
            for s in range(100):
                if m*60+s==targetSeconds:
                    if m>99 or s>99: continue
                    t=str(m*100+s).lstrip('0')
                    if t=="":
                        t="0"
                    ans=min(ans,cost(t))
        
        return ans