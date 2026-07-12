class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        ans=0
        for pattern in patterns:
            if pattern in word:
                ans+=1
        return ans
