class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        x = tomatoSlices - 2*cheeseSlices
        if x < 0 or x % 2: 
            return []
        jumbo = x // 2
        small = cheeseSlices - jumbo
        if small < 0:
            return []
        return [jumbo, small]