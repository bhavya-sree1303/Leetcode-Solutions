class Solution(object):
    def findMissingElements(self, nums):
        s=set(nums)
        mn=min(nums)
        mx=max(nums)
        res=[]
        for i in range(mn,mx+1):
            if i not in s:
                res.append(i)
        return res