
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new = empty // numExchange
            total += new
            empty = empty % numExchange + new

        return total
