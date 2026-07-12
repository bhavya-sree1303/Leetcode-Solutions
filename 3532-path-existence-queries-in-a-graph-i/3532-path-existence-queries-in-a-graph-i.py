class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        group = [0] * n
        g = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                g += 1
            group[i] = g
        
        res = []
        for u, v in queries:
            res.append(group[u] == group[v])
        
        return res