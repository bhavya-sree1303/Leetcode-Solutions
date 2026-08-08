class Solution(object):
    def validSequence(self, word1, word2):
        n,m=len(word1),len(word2)
        
        suf=[0]*(n+1)
        j=m-1
        for i in range(n-1,-1,-1):
            if j>=0 and word1[i]==word2[j]:
                j-=1
            suf[i]=m-1-j
        
        res=[]
        i=j=0
        used=False
        
        while i<n and j<m:
            if word1[i]==word2[j]:
                res.append(i)
                i+=1
                j+=1
            else:
                if not used and suf[i+1]>=m-(j+1):
                    res.append(i)
                    used=True
                    i+=1
                    j+=1
                else:
                    i+=1
        
        return res if j==m else []