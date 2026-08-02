
class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        def cost_to_type(start, time_str):
            cost = 0
            pos = start
            for ch in time_str:
                digit = int(ch)
                if pos != digit:
                    cost += moveCost
                    pos = digit
                cost += pushCost
            return cost

        res = float('inf')

        for m in range(100):
            s = targetSeconds - m * 60
            if 0 <= s <= 99:
                time_str = str(m * 100 + s).rjust(4, '0').lstrip('0') or '0'
                res = min(res, cost_to_type(startAt, time_str))

        return res