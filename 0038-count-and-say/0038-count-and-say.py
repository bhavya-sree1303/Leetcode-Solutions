class Solution(object):
    def countAndSay(self, n):
        s = "1"

        for i in range(n - 1):
            res = ""
            count = 1

            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                else:
                    res += str(count) + s[j - 1]
                    count = 1

            res += str(count) + s[-1]
            s = res

        return s