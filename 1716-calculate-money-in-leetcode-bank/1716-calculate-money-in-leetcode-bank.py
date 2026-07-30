class Solution(object):
    def totalMoney(self, n):
        total=0
        week=0
        for i in range(n):
            day =i % 7
            if day==0:
                week += 1
            total += week + day
        
        return total