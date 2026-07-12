class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10 ** 9 + 7

        m = r - l + 1
        if n == 1:
            return m

        sz = 2 * m

        # state = [up0..up(m-1), down0..down(m-1)]

        # initial vector for length = 2
        vec = [0] * sz
        for v in range(m):
            vec[v] = v                 # up
            vec[m + v] = m - 1 - v     # down

        if n == 2:
            return sum(vec) % MOD

        # transition matrix
        T = [[0] * sz for _ in range(sz)]

        # newUp[v] = prefix of down
        for v in range(m):
            row = v
            for u in range(v):
                T[row][m + u] = 1

        # newDown[v] = suffix of up
        for v in range(m):
            row = m + v
            for u in range(v + 1, m):
                T[row][u] = 1

        def mat_mul(A, B):
            C = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                Ai = A[i]
                Ci = C[i]
                for k in range(sz):
                    if Ai[k] == 0:
                        continue
                    aik = Ai[k]
                    Bk = B[k]
                    for j in range(sz):
                        Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        def mat_vec_mul(A, v):
            res = [0] * sz
            for i in range(sz):
                s = 0
                Ai = A[i]
                for j in range(sz):
                    if Ai[j]:
                        s = (s + Ai[j] * v[j]) % MOD
                res[i] = s
            return res

        p = n - 2

        # binary exponentiation on matrix applied to vector
        while p:
            if p & 1:
                vec = mat_vec_mul(T, vec)
            T = mat_mul(T, T)
            p >>= 1

        return sum(vec) % MOD
        