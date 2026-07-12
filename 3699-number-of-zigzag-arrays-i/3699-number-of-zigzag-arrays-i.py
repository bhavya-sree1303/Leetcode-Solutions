class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1
        up = [1] * m
        down = [1] * m
        for _ in range(1, n):
            new_up = [0] * m
            new_down = [0] * m
            total_up = sum(up) % MOD
            left_up = 0
            left_down = 0
            for i in range(m):
                new_up[i] = left_down % MOD
                new_down[i] = (total_up - left_up - up[i]) % MOD
                left_up += up[i]
                left_down += down[i]
            up, down = new_up, new_down
        return (sum(up) + sum(down)) % MOD