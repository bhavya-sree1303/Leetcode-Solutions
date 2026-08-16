class Solution(object):
    def findPrimePairs(self, n):
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False

        i = 2
        while i * i <= n:
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    prime[j] = False
            i += 1

        ans = []

        for x in range(2, n // 2 + 1):
            y = n - x
            if prime[x] and prime[y]:
                ans.append([x, y])

        return ans