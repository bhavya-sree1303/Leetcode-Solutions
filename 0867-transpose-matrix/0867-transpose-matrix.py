class Solution(object):
    def transpose(self, matrix):
        l=[]
        for i in range(len(matrix[0])):
            s=[]
            for j in range(len(matrix)):
                s.append(matrix[j][i])
            l.append(s)
        return l
        