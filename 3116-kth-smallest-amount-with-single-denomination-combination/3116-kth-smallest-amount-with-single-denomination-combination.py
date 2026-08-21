class Solution:
    def findKthSmallest(self, coins, k):
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        def lcm(a,b):
            return a//gcd(a,b)*b

        def count(x):
            ans=0
            n=len(coins)

            for mask in range(1,1<<n):
                v=1
                bits=0

                for i in range(n):
                    if mask>>i&1:
                        v=lcm(v,coins[i])
                        bits+=1
                        if v>x:
                            break

                if v<=x:
                    if bits%2:
                        ans+=x//v
                    else:
                        ans-=x//v

            return ans

        lo=1
        hi=min(coins)*k

        while lo<hi:
            mid=(lo+hi)//2

            if count(mid)>=k:
                hi=mid
            else:
                lo=mid+1

        return lo