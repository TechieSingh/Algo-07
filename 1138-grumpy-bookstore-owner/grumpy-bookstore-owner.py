class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        value=0
        result=-sys.maxsize - 1
        n=len(customers)
        for i in range(n):
            if grumpy[i]==0:
                value+=customers[i]
        
        for i in range(0,n-minutes+1):
            current_sum=0
            for j in range(minutes):
                if grumpy[i+j]==1:
                    current_sum = current_sum + customers[i + j]
            
            result = max(value+current_sum, result)
        return result
        