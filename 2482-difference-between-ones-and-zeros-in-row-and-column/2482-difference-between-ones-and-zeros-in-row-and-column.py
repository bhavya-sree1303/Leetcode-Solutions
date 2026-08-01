class Solution:
    def onesMinusZeros(self, grid):
        m=len(grid)
        n=len(grid[0])
        r=[0]*m
        c=[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    r[i]+=1
                    c[j]+=1
        res=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j]=2*r[i]+2*c[j]-m-n
        
        return res