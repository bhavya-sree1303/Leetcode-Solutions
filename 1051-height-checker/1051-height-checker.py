class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l=[]
        s=sorted(heights)
        for i in range(0,len(heights)):
            if(heights[i]!=s[i]):
                l.append(i)
        return len(l)
        
        