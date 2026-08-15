class Solution(object):
    def longestSubsequence(self, nums):
        x=0
        for n in nums:
            x^=n
        if x!=0:
            return len(nums)
        for n in nums:
            if n!=0:
                return len(nums)-1
        return 0