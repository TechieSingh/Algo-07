class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip_count = 0  # To keep track of the number of flips
        
        for i in range(n):
            if i >= k and nums[i - k] > 1:
                flip_count ^= 1
                nums[i - k] -= 2
            
            if nums[i] == flip_count:
                if i + k > n:
                    return -1
                flips += 1
                flip_count ^= 1
                nums[i] += 2
        return flips
