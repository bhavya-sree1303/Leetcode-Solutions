class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        res=0
        costs.sort()
        for i in costs:
            if i <= coins:
                coins -= i
                res+= 1
            else:
                break
        return res