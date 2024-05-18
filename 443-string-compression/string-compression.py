from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        n=len(chars)
        result=[]

        while i<n:
            j=i+1
            count=1
            result.append(chars[i])
            while j<n and chars[j]==chars[i]:
                count+=1
                j+=1
            if count>1:
                for digit in str(count):
                    result.append(digit)
            i=j

        chars[:]=result
        return len(chars)




                    



        