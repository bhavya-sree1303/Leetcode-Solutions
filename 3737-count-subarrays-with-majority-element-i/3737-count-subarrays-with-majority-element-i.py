class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        ans=0
        for i in range(n):
            c=0
            for j in range(i,n):
                if nums[j]==target:
                    c+=1
                if ((c*2)>(j-i+1)):
                    ans+=1
        return ans