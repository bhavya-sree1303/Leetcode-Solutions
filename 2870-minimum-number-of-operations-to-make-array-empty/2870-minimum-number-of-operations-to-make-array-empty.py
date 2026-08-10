class Solution(object):
    def minOperations(self, nums):
        from collections import Counter
        
        count = Counter(nums)
        ans = 0
        
        for f in count.values():
            if f == 1:
                return -1
            ans += (f + 2) // 3
        
        return ans