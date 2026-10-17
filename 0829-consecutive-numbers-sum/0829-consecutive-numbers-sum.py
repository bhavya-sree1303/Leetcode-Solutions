
class Solution(object):
    def consecutiveNumbersSum(self, n):
        count = 0
        k = 1

        while k * (k - 1) // 2 < n:
            remaining = n - k * (k - 1) // 2

            if remaining % k == 0:
                count += 1

            k += 1

        return count
