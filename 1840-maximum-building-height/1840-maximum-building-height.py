class Solution(object):
    def maxBuilding(self, n, r):

        r.append([1, 0])
        r.append([n, n - 1])
        r.sort()

        m = len(r)

        for i in range(1, m):
            dist = r[i][0] - r[i - 1][0] 
            r[i][1] = min(r[i][1],r[i - 1][1] + dist)

        for i in range(m - 2, -1, -1):
            dist = r[i + 1][0] - r[i][0]
            r[i][1] = min(r[i][1],r[i + 1][1] + dist)
        ans = 0

        for i in range(1,m):
            id1, h1 = r[i - 1]
            id2, h2 = r[i]
            d = id2 - id1
            ans = max(ans, (h1 + h2 + d) // 2)

        return ans