class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        dup = set()
        for num in nums:
            if num in dup:
                ans.append(num)
            dup.add(num)
        return ans
