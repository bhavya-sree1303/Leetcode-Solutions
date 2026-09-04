class Solution:
    def numSpecial(self, mat):
        count=0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    row=sum(mat[i])
                    col=sum(mat[k][j] for k in range(len(mat)))
                    
                    if row==1 and col==1:
                        count+=1
        
        return count