class Solution(object):
    def passThePillow(self, n, time):
        i, d = 1, 1
        while time:
            time -= 1
            i += d
            if i == 1 or i == n:
                d = -d
        return i
