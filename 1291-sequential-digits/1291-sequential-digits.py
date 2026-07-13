class Solution(object):
    def sequentialDigits(self, low, high):
       res=[]
       s='123456789'
       for length in range(2,10):
          for i in range(0,10-length):
             num=int(s[i:i+length])
             if low<=num<=high:
                res.append(num)
       return sorted(res)

        