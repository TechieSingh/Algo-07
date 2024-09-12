class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(list(allowed))
        count=len(words)
        for word in words:
            if not set(word).issubset(a):
                count-=1
        return count


        