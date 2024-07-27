from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        s = 0
        e = len(nums) - 1
        self.mergeSort(nums, s, e)
        return nums

    def mergeSort(self, nums, s, e):
        if s >= e:
            return
        mid = (s + e) // 2
        self.mergeSort(nums, s, mid)
        self.mergeSort(nums, mid + 1, e)
        self.merge(nums, s, mid, e)

    def merge(self, nums, s, mid, e):
        left = nums[s:mid+1]
        right = nums[mid+1:e+1]

        i = j = 0
        k = s

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
