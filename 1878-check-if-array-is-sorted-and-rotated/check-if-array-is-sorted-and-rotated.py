class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        descents = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                descents += 1
                if descents > 1:
                    return False
        return True
