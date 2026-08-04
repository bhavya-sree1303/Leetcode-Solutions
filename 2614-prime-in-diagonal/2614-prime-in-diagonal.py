class Solution(object):
    def diagonalPrime(self, nums):
        def isPrime(x):
            if x<2:
                return False
            i=2
            while i*i<=x:
                if x%i==0:
                    return False
                i+=1
            return True
        n=len(nums)
        ans=0
        for i in range(n):
            a=nums[i][i]
            b=nums[i][n-i-1]
            if isPrime(a):
                ans=max(ans,a)
            if isPrime(b):
                ans=max(ans,b)
        return ans