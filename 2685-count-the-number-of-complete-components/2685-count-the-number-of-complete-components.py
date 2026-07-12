class Solution(object):
    def countCompleteComponents(self, n, edges):
        graph = [[] for i in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        
        def dfs(node):
            stack = [node]
            nodes = 0
            edge_count = 0
            
            while stack:
                curr = stack.pop()
                if visited[curr]:
                    continue
                visited[curr] = True
                nodes += 1
                edge_count += len(graph[curr])
                
                for nei in graph[curr]:
                    if not visited[nei]:
                        stack.append(nei)
            
            return nodes, edge_count // 2
        
        ans = 0
        
        for i in range(n):
            if not visited[i]:
                nodes, edges_count = dfs(i)
                if edges_count == nodes * (nodes - 1) // 2:
                    ans += 1
        
        return ans