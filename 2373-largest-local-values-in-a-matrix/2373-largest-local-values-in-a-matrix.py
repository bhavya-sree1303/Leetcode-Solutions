class Solution(object):
    def largestLocal(self, grid):
        n=len(grid)
        res=[]
        for i in range(n-2):
            row=[]
            for j in range(n-2):
                m=0
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        m=max(m,grid[x][y])
                row.append(m)
            res.append(row)
        return res