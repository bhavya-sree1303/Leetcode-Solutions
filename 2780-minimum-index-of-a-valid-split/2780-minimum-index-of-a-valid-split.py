class Solution(object):
    def minimumIndex(self, nums):
        n = len(nums)

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        dominant = 0
        total = 0

        for num in count:
            if count[num] > total:
                dominant = num
                total = count[num]

        leftCount = 0

        for i in range(n - 1):
            if nums[i] == dominant:
                leftCount += 1

            leftLength = i + 1
            rightLength = n - leftLength
            rightCount = total - leftCount

            if 2 * leftCount > leftLength and 2 * rightCount > rightLength:
                return i

        return -1