from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m,n=len(classroom),len(classroom[0])
        litter={}
        sr=sc=0
        k=0

        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S':
                    sr,sc=i,j
                elif classroom[i][j]=='L':
                    litter[(i,j)]=k
                    k+=1

        if k==0:
            return 0

        full=(1<<k)-1
        q=deque([(sr,sc,0,energy,0)])
        best={(sr,sc,0):energy}
        dirs=((1,0),(-1,0),(0,1),(0,-1))

        while q:
            r,c,mask,e,d=q.popleft()

            for dr,dc in dirs:
                nr,nc=r+dr,c+dc

                if nr<0 or nr>=m or nc<0 or nc>=n:
                    continue
                if classroom[nr][nc]=='X':
                    continue
                if e==0:
                    continue

                ne=e-1
                nm=mask

                if (nr,nc) in litter:
                    nm|=1<<litter[(nr,nc)]

                if classroom[nr][nc]=='R':
                    ne=energy

                if nm==full:
                    return d+1

                key=(nr,nc,nm)

                if ne>best.get(key,-1):
                    best[key]=ne
                    q.append((nr,nc,nm,ne,d+1))

        return -1