class Solution(object):
    def superpalindromesInRange(self, left, right):
        l = int(left)
        r = int(right)
        count = 0

        for i in range(1, 100000):
            s = str(i)
            p = int(s + s[-2::-1])
            q = int(s + s[::-1])

            for x in (p, q):
                sq = x * x

                if sq > r:
                    continue

                if sq >= l and str(sq) == str(sq)[::-1]:
                    count += 1

        return count