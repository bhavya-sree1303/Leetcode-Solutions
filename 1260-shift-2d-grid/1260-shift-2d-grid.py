class Solution(object):
    def shiftGrid(self, grid, k):
        m=len(grid)
        n=len(grid[0])
        for i in range(k):
            prev=grid[m-1][n-1]
            for i in range(m):
                for j in range(n):
                    temp=grid[i][j]
                    grid[i][j]=prev
                    prev=temp
        return grid