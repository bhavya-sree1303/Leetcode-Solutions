class Solution:
    def diagonalSum(self, mat):
        n=len(mat)
        s=0
        for i in range(n):
            s+=mat[i][i]+mat[i][n-1-i]
        if n%2==1:
            s-=mat[n//2][n//2]
        return s