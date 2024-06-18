class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        result = 0
        value = 0
        worker.sort()
        jobs = sorted(zip(difficulty, profit))
        j = 0
        
        for w in worker:
            while j < len(jobs) and w >= jobs[j][0]:
                value = max(jobs[j][1], value)
                j += 1
            result += value
        
        return result

