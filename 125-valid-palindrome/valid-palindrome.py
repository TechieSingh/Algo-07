class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        ls = re.sub(r'[^a-zA-Z0-9]', '', s)
        ls=ls.lower()
        return ls==ls[::-1]



        