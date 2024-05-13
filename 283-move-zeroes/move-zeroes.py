class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        i=0
        no_zero=0
        while(i<n):
            if nums[i]!=0:
                nums[no_zero]=nums[i]
                no_zero+=1
            i+=1
        while(no_zero<n):
            nums[no_zero]=0
            no_zero+=1