class Solution(object):
    def smallestSubsequence(self, s):
        top = -1
        freq = {}
        seen = set()
        ans = []
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in s:
            freq[ch] -= 1
            if ch in seen:
                continue
            while top >= 0 and ch < ans[top] and freq[ans[top]] > 0:
                seen.remove(ans.pop())
                top -= 1
            ans.append(ch)
            seen.add(ch)
            top += 1
        return ''.join(ans)
