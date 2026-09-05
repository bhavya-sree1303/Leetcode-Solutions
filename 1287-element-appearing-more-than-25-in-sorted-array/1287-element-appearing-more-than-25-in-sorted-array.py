class Solution:
    def findSpecialInteger(self, arr):
        n = len(arr)
        count = 1
        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                count += 1
            else:
                count = 1
            if count * 4 >n:
                return arr[i]
        return arr[0]