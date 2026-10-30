class Solution(object):
    def decodeMessage(self, key, message):
        d = {}
        j = 0

        for ch in key:
            if ch != ' ' and ch not in d:
                d[ch] = chr(97 + j)
                j += 1

        res = ""

        for ch in message:
            if ch == ' ':
                res += ' '
            else:
                res += d[ch]

        return res