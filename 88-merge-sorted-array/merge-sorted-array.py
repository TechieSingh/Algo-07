class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=m
        while i<n:
            nums1[j]=nums2[i]
            j+=1
            i+=1
        r=m+n
        for p in range(r):
            for k in range(1,r-p):
                if nums1[k-1]>nums1[k]:
                    nums1[k-1],nums1[k]=nums1[k],nums1[k-1]