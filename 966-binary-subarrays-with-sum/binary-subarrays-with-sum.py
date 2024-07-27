class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = defaultdict(int)
        d[0]=1
        res=cur=0
        for i in nums:
            cur+=i%2
            res+=d[cur-goal]
            d[cur]+=1
        return res