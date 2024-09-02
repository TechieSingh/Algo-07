class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)  # Calculate the total chalk used in one complete round
        k %= total  # Reduce k to be within one complete round
        
        for i, value in enumerate(chalk):
            if value > k:
                return i
            k -= value  # Subtract chalk used by each student

        