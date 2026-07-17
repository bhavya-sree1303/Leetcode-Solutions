class Solution(object):
    def gcdValues(self, nums, queries):
        from bisect import bisect_left
        
        maxv = max(nums)
        
        freq = [0] * (maxv + 1)
        for x in nums:
            freq[x] += 1
        
        cnt = [0] * (maxv + 1)
        
        for g in range(maxv, 0, -1):
            total = 0
            for m in range(g, maxv + 1, g):
                total += freq[m]
            
            cnt[g] = total * (total - 1) // 2
            
            for m in range(2 * g, maxv + 1, g):
                cnt[g] -= cnt[m]
        
        pref = []
        s = 0
        for g in range(1, maxv + 1):
            if cnt[g]:
                s += cnt[g]
                pref.append((s, g))
        
        ans = []
        for q in queries:
            i = bisect_left(pref, (q + 1, 0))
            ans.append(pref[i][1])
        
        return ans