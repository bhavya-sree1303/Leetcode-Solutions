class Solution(object):
    def alternatingSubarray(self, nums):
        n = len(nums)
        maxLen = -1
        length = 1

        for i in range(1, n):
            if length == 1:
                if nums[i] == nums[i - 1] + 1:
                    length = 2
                else:
                    length = 1
            else:
                if nums[i] == nums[i - 2]:
                    length += 1
                else:
                    if nums[i] == nums[i - 1] + 1:
                        length = 2
                    else:
                        length = 1

            if length >= 2:
                maxLen = max(maxLen, length)

        return maxLen