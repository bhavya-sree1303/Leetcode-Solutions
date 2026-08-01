class Solution:
    def largestTriangleArea(self, points):
        n = len(points)
        ans = 0.0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    area = abs(
                        (x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)
                    ) / 2.0
                    ans = max(ans, area)

        return ans