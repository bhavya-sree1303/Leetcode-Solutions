class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):

        hBars.sort()
        vBars.sort()

        h = 1
        v = 1

        count = 1

        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                count += 1
            else:
                count = 1

            h = max(h, count)

        count = 1

        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                count += 1
            else:
                count = 1

            v = max(v, count)

        side = min(h, v) + 1

        return side * side