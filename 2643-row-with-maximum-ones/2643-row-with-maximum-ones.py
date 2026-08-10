class Solution(object):
    def rowAndMaximumOnes(self, mat):
        maxCount = 0
        rowIndex = 0
        
        for i in range(len(mat)):
            count = sum(mat[i])
            if count > maxCount:
                maxCount = count
                rowIndex = i
        
        return [rowIndex, maxCount]