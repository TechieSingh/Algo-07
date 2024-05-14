class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=len(num)
        val=0
        result=[]
        for i in range(n):
            val+=num[i]*10**(n-i-1)
        val+=k
        while(val!=0):
            result.append(val%10)
            val=val//10
        return result[::-1]
        