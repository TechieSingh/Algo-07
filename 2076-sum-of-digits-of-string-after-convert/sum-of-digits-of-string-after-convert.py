class Solution:
    def getLucky(self, s: str, k: int) -> int:
        covt = []
        for char in s:
            num = ord(char) - ord('a') + 1  
            covt.extend(map(int, str(num))) 
        def transform(covt, k):
            if k == 1:
                return sum(covt)  
            else:
                temp = sum(covt)  
                covt = list(map(int, str(temp)))  
                return transform(covt, k - 1)  
        return transform(covt, k)
