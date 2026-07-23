class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for ele in nums:
            if(len(str(ele))>1):
                ele=str(ele)
                for e in ele:
                    l.append(int(e))
            else:
                l.append(int(ele))
        return l