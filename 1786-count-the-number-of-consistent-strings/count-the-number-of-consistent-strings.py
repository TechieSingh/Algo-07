class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(list(allowed))
        count=len(words)
        for each in words:
            b=set(list(each))
            if not b.issubset(a):
                count-=1
        return count


        