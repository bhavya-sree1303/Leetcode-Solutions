from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        # Collect sorted unique edge costs for binary search
        costs = sorted(set(c for _, _, c in edges))
        if not costs:
            return -1
        
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, c in edges:
            adj[u].append((v, c))
        
        # Compute topological order once (the graph is a DAG)
        indeg = [0] * n
        for u in range(n):
            for v, _ in adj[u]:
                indeg[v] += 1
        
        topo_order = []
        q = deque([u for u in range(n) if indeg[u] == 0])
        indeg_topo = indeg[:]  # copy to mutate
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v, _ in adj[u]:
                indeg_topo[v] -= 1
                if indeg_topo[v] == 0:
                    q.append(v)
        
        # Sort each node's outgoing edges by cost descending (for early break)
        for u in range(n):
            adj[u].sort(key=lambda x: -x[1])
        
        def can_achieve(min_edge: int) -> bool:
            """Check if there exists a path from 0 to n-1 using only edges
            with cost >= min_edge, passing only through online nodes,
            with total path cost <= k."""
            
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo_order:
                if dist[u] == float('inf'):
                    continue
                # Node u must be online (or it's the source node 0)
                if not online[u] and u != 0:
                    continue
                
                for v, c in adj[u]:
                    if c < min_edge:
                        break  # remaining edges have even smaller costs
                    # Node v must be online (or it's the destination n-1)
                    if not online[v] and v != n - 1:
                        continue
                    
                    nd = dist[u] + c
                    if nd < dist[v]:
                        dist[v] = nd
            
            return dist[n - 1] <= k
        
        # Binary search on sorted unique costs
        lo, hi = 0, len(costs) - 1
        ans = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_achieve(costs[mid]):
                ans = costs[mid]
                lo = mid + 1  # try for a larger score
            else:
                hi = mid - 1
        
        return ans