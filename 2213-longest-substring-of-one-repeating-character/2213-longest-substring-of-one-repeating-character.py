class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n=len(s)
        s=list(s)
        size=1
        while size<n:
            size*=2

        tree=[(0,0,0,0,'','') for _ in range(2*size)]

        def merge(a,b):
            if a[0]==0:
                return b
            if b[0]==0:
                return a

            length=a[0]+b[0]
            left=a[4]
            right=b[5]

            pref=a[1]
            suff=b[2]
            best=max(a[3],b[3])

            if a[5]==b[4]:
                best=max(best,a[2]+b[1])

                if a[1]==a[0]:
                    pref=a[0]+b[1]

                if b[2]==b[0]:
                    suff=b[0]+a[2]

            return (length,pref,suff,best,left,right)

        for i in range(n):
            tree[size+i]=(1,1,1,1,s[i],s[i])

        for i in range(size-1,0,-1):
            tree[i]=merge(tree[2*i],tree[2*i+1])

        def update(pos,c):
            p=size+pos
            tree[p]=(1,1,1,1,c,c)
            p//=2

            while p:
                tree[p]=merge(tree[2*p],tree[2*p+1])
                p//=2

        ans=[]

        for c,i in zip(queryCharacters,queryIndices):
            update(i,c)
            ans.append(tree[1][3])

        return ans