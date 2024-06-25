class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flip_window = [0] * n
        flip_count = 0
        
        for i in range(n):
            if i >= k:
                flip_count ^= flip_window[i - k]
            
            if nums[i] == flip_count:
                if i + k > n:
                    return -1
                flips += 1
                flip_count ^= 1
                flip_window[i] = 1
        
        return flips
