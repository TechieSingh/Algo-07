class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}

        for i,num in enumerate(nums):
            val=target-num
            if val in hash:
                return [hash[val],i]  
            hash[num]=i
        