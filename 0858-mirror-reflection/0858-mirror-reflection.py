class Solution(object):
    def mirrorReflection(self, p, q):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        g = gcd(p, q)
        p //= g
        q //= g
        if p % 2 == 0:
            return 2
        if q % 2 == 0:
            return 0
        return 1