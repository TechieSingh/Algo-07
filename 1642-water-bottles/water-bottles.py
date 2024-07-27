class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result=numBottles
        while numBottles>=numExchange:
            newfull=numBottles//numExchange
            result+=newfull
            numBottles=(numBottles%numExchange)+(newfull)
        return result


        