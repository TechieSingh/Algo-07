class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=m
        while i<n:
            nums1[j]=nums2[i]
            j+=1
            i+=1
        nums1.sort()