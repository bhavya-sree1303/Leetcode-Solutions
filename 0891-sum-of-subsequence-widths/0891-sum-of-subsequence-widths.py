
class Solution(object):
    def sumSubseqWidths(self, nums):
        mod = 10**9 + 7
        nums.sort()

        n = len(nums)
        ans = 0
        power = 1

        for i in range(n):
            ans = (ans + nums[i] * (power - pow(2, n - 1 - i, mod))) % mod
            power = (power * 2) % mod

        return ans
