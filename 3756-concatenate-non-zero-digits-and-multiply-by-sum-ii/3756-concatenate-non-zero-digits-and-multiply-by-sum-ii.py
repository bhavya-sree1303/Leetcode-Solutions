from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        Mod = 10**9 + 7
        
        pos = []
        digits = []
        
        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))
        
        n = len(digits)
        
        prefix_sum = [0] * (n + 1)
        prefix_num = [0] * (n + 1)
        pow10 = [1] * (n + 1)
        
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % Mod
        
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + digits[i]
            prefix_num[i+1] = (prefix_num[i] * 10 + digits[i]) % Mod
        
        ans = []
        
        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r)
            
            length = right - left
            
            if length == 0:
                ans.append(0)
                continue
            
            c = prefix_sum[right] - prefix_sum[left]
            res = (prefix_num[right] - prefix_num[left] * pow10[length]) % Mod
            
            ans.append((res * c) % Mod)
        
        return ans


