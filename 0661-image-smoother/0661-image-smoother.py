class Solution:
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])
        ans = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                total=0
                count=0
                for r in range(i-1,i+2):
                    for c in range(j-1,j+2):
                        if 0<=r<m and 0<=c<n:
                            total+=img[r][c]
                            count+=1
                ans[i][j]=total//count

        return ans