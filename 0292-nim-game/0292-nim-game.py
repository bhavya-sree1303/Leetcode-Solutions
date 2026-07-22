class Solution(object):
    def canWinNim(self, n):
        if n<=3:
            return True
        return n%4!=0
        
        