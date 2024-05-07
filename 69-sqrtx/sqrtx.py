class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0,x
        if x<2:
            return x
        while low<=high:
            mid=(low+high)//2
            mid_sqr = mid*mid
            if mid_sqr==x:
                return mid
            elif mid_sqr<x:
                low = mid+1
            else:
                high = mid-1
        return high
        