class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        l=0
        ans=0
        ls=set()
        for i in range(n):
            while s[i] in ls:
                ls.remove(s[l])
                l+=1
            ls.add(s[i])
            ans=max(ans,i-l+1)
        return ans