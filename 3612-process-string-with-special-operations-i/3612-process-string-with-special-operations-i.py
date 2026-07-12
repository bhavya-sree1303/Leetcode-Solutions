class Solution(object):
    def processStr(self, s):
        result=""
        for ch in s:
          if 'a'<= ch <='z':
            result+=ch
          elif(ch=='#'):
            result+=result
          elif(ch=='*'):
            result=result[:-1]
          elif(ch=='%'):
            result=result[::-1]
            #"".join(reversed(result))
        return result
        