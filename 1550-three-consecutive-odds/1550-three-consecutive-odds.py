class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr)-2):
            a=arr[i]
            b=arr[i+1]
            c=arr[i+2]
            if a%2 and b%2 and c%2:
                return True
        return False