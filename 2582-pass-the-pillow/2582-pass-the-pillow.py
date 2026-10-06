class Solution(object):
    def passThePillow(self, n, time):
        cycle = 2 * (n - 1)
        time = time % cycle

        if time < n:
            return time + 1
        else:
            return 2 * n - time - 1