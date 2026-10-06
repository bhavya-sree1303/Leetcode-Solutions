class Solution(object):
    def makeSubKSumEqual(self, arr, k):
        n = len(arr)

        a = n
        b = k

        while b != 0:
            a, b = b, a % b

        g = a
        answer = 0

        for i in range(g):
            values = []
            j = i

            while j < n:
                values.append(arr[j])
                j += g

            values.sort()
            median = values[len(values) // 2]

            for x in values:
                answer += abs(x - median)

        return answer