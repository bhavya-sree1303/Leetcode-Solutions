class Solution:
    def deleteGreatestValue(self, grid):
        for row in grid:
            row.sort()
        ans=0
        for col in range(len(grid[0])-1,-1,-1):
            m=0
            for row in grid:
                m=max(m,row[col])
            ans+=m
        return ans