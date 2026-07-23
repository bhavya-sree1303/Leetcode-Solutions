class Solution(object):
    def uniqueXorTriplets(self, nums):
       n=len(nums)
       if n<3:
         return n
       k=n.bit_length()
       return 2**k