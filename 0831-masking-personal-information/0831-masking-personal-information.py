
class Solution(object):
    def maskPII(self, s):
        if '@' in s:
            a, b = s.split('@')
            a = a.lower()
            b = b.lower()

            return a[0] + "*****" + a[-1] + "@" + b

        else:
            digits = ""

            for ch in s:
                if ch.isdigit():
                    digits += ch

            n = len(digits)

            if n == 10:
                return "***-***-" + digits[-4:]
            else:
                return "+" + "*" * (n-10) + "-***-***-" + digits[-4:]
