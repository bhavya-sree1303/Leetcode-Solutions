class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = []
        for i in range(n):
            arr.append([
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            ])

        arr.sort(key=lambda x: (x[0], x[1]))

        starts = [arr[i][0] for i in range(n)]

        next_index = [0] * n

        for i in range(n):
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2

                if starts[mid] > arr[i][1]:
                    right = mid
                else:
                    left = mid + 1

            next_index[i] = left

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for k in range(1, 5):

                skip = dp[i + 1][k]

                j = next_index[i]
                future = dp[j][k - 1]

                indices = tuple(sorted((arr[i][3],) + future[1]))

                take = (
                    arr[i][2] + future[0],
                    indices
                )

                if take[0] > skip[0]:
                    dp[i][k] = take

                elif take[0] < skip[0]:
                    dp[i][k] = skip

                else:
                    if take[1] < skip[1]:
                        dp[i][k] = take
                    else:
                        dp[i][k] = skip

        return list(dp[0][4][1])