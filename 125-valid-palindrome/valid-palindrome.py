class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        ls = re.sub(r'[^a-zA-Z0-9]', '', s)
        ls=ls.lower()
        print(ls) 
        p=len(ls)       
        for k in range(p):
            if ls[k]!=ls[p-1-k]:
                return False
        return True



        