class Solution(object):
    def maxChunksToSorted(self, arr):
        chunks = 0
        maximum = 0

        for i in range(len(arr)):
            maximum = max(maximum, arr[i])

            if maximum == i:
                chunks += 1

        return chunks