from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        # dp[i][j] = [max_score, ways]
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Start from 'S'
        dp[n-1][n-1] = [0, 1]
        
        # Fill the DP table
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                if board[i][j] == 'X':
                    continue
                
                if i == n-1 and j == n-1:
                    continue
                
                max_score = -1
                ways = 0
                
                # Check 3 possible moves
                for ni, nj in [(i+1, j), (i, j+1), (i+1, j+1)]:
                    if 0 <= ni < n and 0 <= nj < n:
                        score, w = dp[ni][nj]
                        
                        if score == -1:
                            continue
                        
                        if score > max_score:
                            max_score = score
                            ways = w
                        elif score == max_score:
                            ways = (ways + w) % MOD
                
                if max_score == -1:
                    continue
                
                # Add current cell value
                if board[i][j] not in ('S', 'E'):
                    max_score += int(board[i][j])
                
                dp[i][j] = [max_score, ways]
        
        # Final answer at 'E'
        if dp[0][0][0] == -1:
            return [0, 0]
        
        return dp[0][0]