class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        work = [] 
        ans = []  
        if False:
            b = self.L0238(nums, ans, work, "Brute Force")
        if False:
            b = self.L0238(nums, ans, work, "Use Division")
        if False:
            b = self.L0238(nums, ans, work, "n time n space")
        if True:
            b = self.L0238(nums, ans, work, "n time 1 space")
        
        return ans

    def L0238(self, nums, ans, work, method):
        print(f"Processing with method: {method}")
        if method == "Brute Force":
            for i in range(len(nums)):
                product = 1
                for j in range(len(nums)):
                    if i != j:
                        product *= nums[j]
                ans.append(product)
        
        elif method == "Use Division":
            total_product = 1
            for num in nums:
                if num != 0:
                    total_product *= num
            for num in nums:
                if num != 0:
                    ans.append(total_product // num)
                else:
                    ans.append(0)  
        
        elif method == "n time n space":
            left = [1] * len(nums)
            right = [1] * len(nums)
            for i in range(1, len(nums)):
                left[i] = left[i-1] * nums[i-1]
            for i in range(len(nums) - 2, -1, -1):
                right[i] = right[i+1] * nums[i+1]
            for i in range(len(nums)):
                ans.append(left[i] * right[i])
        
        elif method == "n time 1 space":
            ans.extend([1] * len(nums))
            left = 1
            for i in range(len(nums)):
                ans[i] = left
                left *= nums[i]
            right = 1
            for i in range(len(nums) - 1, -1, -1):
                ans[i] *= right
                right *= nums[i]

        return ans
