class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_capital_heap = []
        max_profit_heap = []
        
        for i in range(len(profits)):
            heapq.heappush(min_capital_heap, (capital[i], profits[i]))
        
        for _ in range(k):
            while min_capital_heap and min_capital_heap[0][0] <= w:
                cap, prof = heapq.heappop(min_capital_heap)
                heapq.heappush(max_profit_heap, -prof)
            
            if not max_profit_heap:
                break
            
            w += -heapq.heappop(max_profit_heap)
        
        return w
        