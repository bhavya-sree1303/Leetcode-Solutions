class Solution:
    def numPrimeArrangements(self, n):
        MOD=10**9+7
        p=0
        for x in range(2,n+1):
            prime=True
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    prime=False
                    break
            if prime:
                p+=1
        a=1
        for i in range(1,p+1):
            a=a*i%MOD
        b=1
        for i in range(1,n-p+1):
            b=b*i%MOD
        return a*b%MOD