
class Solution(object):
    def matrixSum(self, nums):
        for row in nums:
            row.sort()

        score = 0

        for i in range(len(nums[0])):
            largest = 0

            for j in range(len(nums)):
                largest = max(largest, nums[j][i])

            score += largest

        return score
