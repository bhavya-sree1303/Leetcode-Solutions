class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        n = len(nums)
        ans = 0
        length = 0

        for i in range(n):
            if nums[i] > threshold:
                length = 0
            elif length == 0:
                if nums[i] % 2 == 0:
                    length = 1
                else:
                    length = 0
            else:
                if nums[i] % 2 != nums[i - 1] % 2:
                    length += 1
                else:
                    length = 0
                    if nums[i] % 2 == 0:
                        length = 1

            ans = max(ans, length)

        return ans