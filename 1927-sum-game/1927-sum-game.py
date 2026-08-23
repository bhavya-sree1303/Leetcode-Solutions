class Solution:
    def sumGame(self, num):
        n=len(num)//2
        left=right=l=r=0
        for i in range(n):
            if num[i]=='?':
                l+=1
            else:
                left+=int(num[i])
        for i in range(n,2*n):
            if num[i]=='?':
                r+=1
            else:
                right+=int(num[i])
        if l==r:
            return left!=right
        if l>r:
            return left-right+(l-r)*4.5!=0
        return left-right+(l-r)*4.5!=0