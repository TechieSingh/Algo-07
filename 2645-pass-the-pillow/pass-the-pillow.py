class Solution(object):
    def passThePillow(self, n, time):
        val = time % (n - 1)
        if (time // (n - 1)) % 2 == 0:
            return val + 1
        else:
            return n - val

