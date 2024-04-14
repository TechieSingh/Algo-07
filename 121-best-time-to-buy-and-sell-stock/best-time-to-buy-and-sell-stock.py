class Solution(object):
    def maxProfit(self, prices):
        min,max,profit = prices[0],prices[0],0
        for x in prices:
            if x<min:
                min=x
                max=0
            elif x>max:
                max=x
                if max - min > profit:
                    profit = max - min
                    
        return profit