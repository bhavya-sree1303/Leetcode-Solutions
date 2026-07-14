class Solution(object):
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        
        # custom gcd (safe for all Python versions)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # dp[(g1, g2)] = number of ways
        dp = {(0, 0): 1}
        
        for num in nums:
            new_dp = dp.copy()
            
            for (g1, g2), count in dp.items():
                
                # Put num in seq1
                ng1 = num if g1 == 0 else gcd(g1, num)
                new_dp[(ng1, g2)] = (new_dp.get((ng1, g2), 0) + count) % MOD
                
                # Put num in seq2
                ng2 = num if g2 == 0 else gcd(g2, num)
                new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + count) % MOD
                
                # Skip → already included
            
            dp = new_dp
        
        ans = 0
        
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + count) % MOD
        
        return ans
        