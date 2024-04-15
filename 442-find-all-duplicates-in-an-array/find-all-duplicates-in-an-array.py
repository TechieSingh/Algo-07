class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        for num in nums:
            index = abs(num) - 1  # Get the index corresponding to the number
            if nums[index] < 0:
                ans.append(abs(num))  # If the number at this index is negative, it means it has appeared before
            else:
                nums[index] = -nums[index]  # Mark the number as visited by using logical NOT gate (negation)

        return ans
