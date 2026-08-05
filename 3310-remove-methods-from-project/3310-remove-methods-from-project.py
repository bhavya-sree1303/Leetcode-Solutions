from collections import deque
class Solution:
    def remainingMethods(self,n,k,inv):
        g=[[]for _ in range(n)]
        for a,b in inv:
            g[a].append(b)
        
        vis=[0]*n
        q=deque([k])
        vis[k]=1
        while q:
            u=q.popleft()
            for v in g[u]:
                if not vis[v]:
                    vis[v]=1
                    q.append(v)
        for a,b in inv:
            if not vis[a] and vis[b]:
                return list(range(n))

        return [i for i in range(n) if not vis[i]]       