class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans=[0]* n

        for i in range(n):
            ans[i]=nums[i]

        return ans+ans

        