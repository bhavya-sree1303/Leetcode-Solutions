class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        res=1
        for i in range(1,len(arr)):
            if(arr[i]>=res+1):
                res=res+1
        return res
        
        