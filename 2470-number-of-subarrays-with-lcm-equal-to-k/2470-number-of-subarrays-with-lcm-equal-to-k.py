class Solution(object):
    def subarrayLCM(self, nums, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        count = 0
        for i in range(len(nums)):
            lcm = 1
            for j in range(i, len(nums)):
                lcm = lcm * nums[j] // gcd(lcm, nums[j])
                if lcm == k:
                    count += 1
                elif lcm > k or k % lcm != 0:
                    break

        return count
        