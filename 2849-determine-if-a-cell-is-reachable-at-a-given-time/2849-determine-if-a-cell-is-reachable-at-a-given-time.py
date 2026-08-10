class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        dx = abs(fx - sx)
        dy = abs(fy - sy)
        
        if dx == 0 and dy == 0 and t == 1:
            return False
        
        return max(dx, dy) <= t