class Solution(object):
    def oddString(self, words):
        def diff(s):
            return [ord(s[i+1]) - ord(s[i]) for i in range(len(s)-1)]

        a = diff(words[0])
        b = diff(words[1])
        c = diff(words[2])

        if a == b:
            for w in words:
                if diff(w) != a:
                    return w
        elif a == c:
            return words[1]
        else:
            return words[0]