class Solution(object):
    def processStr(self, s, k):

        lengths = [0]

        for ch in s:
            cur = lengths[-1]

            if 'a' <= ch <= 'z':
                cur += 1
            elif ch == '#':
                cur *= 2
            elif ch == '*':
                if cur > 0:
                    cur -= 1

            lengths.append(cur)

        if k >= lengths[-1]:
            return '.'

        n = len(s)

        for i in range(n - 1, -1, -1):

            ch = s[i]
            before = lengths[i]
            after = lengths[i + 1]

            if 'a' <= ch <= 'z':
                if k == before:
                    return ch

            elif ch == '#':
                half = before
                if k >= half:
                    k -= half

            elif ch == '%':
                k = after - 1 - k

        return '.'
        