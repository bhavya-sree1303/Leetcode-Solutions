class Solution(object):
    def alternateDigitSum(self, n):
        s=str(n)
        sign=1
        res=0
        for ch in s:
            res+=sign*int(ch)
            sign*=-1
        return res