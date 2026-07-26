class Solution(object):
    def isHappy(self, n):
        while n!=1 and n!=4:
            s=0
            while n!=0:
                s=s+(n%10)**2
                n=n//10
            n=s
        if(n==1):
            return True
        return False
        