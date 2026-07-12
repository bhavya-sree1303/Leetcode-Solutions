from typing import List
from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Directions: up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Adjust initial health
        start_health = health - grid[0][0]
        if start_health < 1:
            return False
        
        # visited[r][c] = max health we've had at this cell
        visited = [[-1]*n for _ in range(m)]
        visited[0][0] = start_health
        
        queue = deque([(0, 0, start_health)])
        
        while queue:
            r, c, h = queue.popleft()
            
            # If reached destination
            if r == m-1 and c == n-1:
                return True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_health = h - grid[nr][nc]
                    
                    if new_health >= 1 and visited[nr][nc] < new_health:
                        visited[nr][nc] = new_health
                        queue.append((nr, nc, new_health))
        
        return False
        