class Solution(object):
    def sumAndMultiply(self, n):
        res=0
        c=0
        s=str(n)
        for ch in s:
            if ch!='0':
                digit=int(ch)
                c+=digit
                res=res*10+digit
        return res*c

        