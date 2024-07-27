class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        res = cur = 0
        for i in nums:
            cur += i % 2
            res += d[cur - k]
            d[cur] += 1
        return res
        