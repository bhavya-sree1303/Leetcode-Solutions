class Solution(object):
    def canBeIncreasing(self, nums):
        c=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                c+=1
                if c>1:
                    return False
                if i>1 and nums[i]<=nums[i-2]:
                    nums[i]=nums[i-1]
        return True