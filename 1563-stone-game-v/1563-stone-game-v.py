class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        from functools import lru_cache

        n = len(stoneValue)
        pre = [0] * (n + 1)

        for i in range(n):
            pre[i + 1] = pre[i] + stoneValue[i]

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return 0

            ans = 0
            left = 0
            right = pre[j + 1] - pre[i]

            for k in range(i, j):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    if ans >= left * 2:
                        continue
                    ans = max(ans, left + dp(i, k))

                elif left > right:
                    if ans >= right * 2:
                        break
                    ans = max(ans, right + dp(k + 1, j))

                else:
                    ans = max(ans, left + dp(i, k), right + dp(k + 1, j))

            return ans

        return dp(0, n - 1)