class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
        
        total = [0]*(n+1)
        for i in range(n-1, -1, -1):
            total[i] = total[i+1] + piles[i]
        
        dp = {}
        
        def solve(i, M):
            if i >= n:
                return 0
            
            if (i, M) in dp:
                return dp[(i, M)]
            
            if i + 2*M >= n:
                return total[i]
            
            best = 0
            
            for x in range(1, 2*M + 1):
                opponent = solve(i + x, max(M, x))
                current = total[i] - opponent
                best = max(best, current)
            
            dp[(i, M)] = best
            return best
        
        return solve(0, 1)