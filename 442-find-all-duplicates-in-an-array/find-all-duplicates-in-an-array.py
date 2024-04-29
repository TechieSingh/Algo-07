class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        dup = set()
        for num in nums:
            if num in dup:
                ans.append(num)
            dup.add(num)
        return ans
        