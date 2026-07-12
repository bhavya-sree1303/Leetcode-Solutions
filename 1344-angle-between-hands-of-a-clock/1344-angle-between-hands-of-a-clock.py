class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_angle = hour  * 30 + minutes * 0.5
        minute_angle = 6 * minutes
        diff = abs(hour_angle - minute_angle)
        return min(diff , 360 - diff)
        