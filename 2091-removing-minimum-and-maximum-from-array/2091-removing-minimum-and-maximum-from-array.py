class Solution:
    def minimumDeletions(self, nums):
        n=len(nums)
        i=nums.index(min(nums))
        j=nums.index(max(nums))
        l=min(i,j)
        r=max(i,j)
        return min(r+1,n-l,l+1+n-r)