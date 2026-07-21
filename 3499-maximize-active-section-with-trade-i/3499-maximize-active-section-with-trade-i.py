class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        t = '1' + s + '1'
        ones = s.count('1')
        
        # build groups
        g = []
        c = []
        
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            g.append(j - i)
            c.append(t[i])
            i = j
        
        ans = ones
        
        # check all 0-1-0
        for i in range(len(g) - 2):
            if c[i] == '0' and c[i+1] == '1' and c[i+2] == '0':
                ans = max(ans, ones + g[i] + g[i+2])
        
        return ans