class Solution:
    def countDigits(self, num):
        c=0
        for d in str(num):
            if num % int(d)==0:
                c += 1
        return c