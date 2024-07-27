class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j=int(c**0.5)
        i=0
        while i<=j:
            val =i*i + j*j
            if val == c:
                return True
            elif val<c:
                i+=1
            else:
                j-=1
        return False

        