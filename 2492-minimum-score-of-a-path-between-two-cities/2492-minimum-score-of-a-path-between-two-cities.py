class Solution(object):
    def minScore(self, n, roads):
       graph={i:[] for i in range(1,n+1)}
       for u,v,d in roads:
          graph[u].append((v,d))
          graph[v].append((u,d))
       visited={1}
       stack=[1]
       ans=float('infinity')
       while stack:
          node=stack.pop()
          for neighbour,d in graph[node]:
            ans=min(ans,d)
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
       return ans