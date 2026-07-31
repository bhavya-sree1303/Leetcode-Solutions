class Solution(object):
    def minimumPushes(self, word):
        from collections import Counter
        freq=sorted(Counter(word).values(),reverse=True)
        res=0
        for i in range(len(freq)):
            res+=freq[i]*(i//8+1)
        return res