class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(list(allowed))
        count=len(words)
        for each in words:
            b=set(list(each))
            for i in b:
                if i not in a:
                    count-=1
                    break

        return count


        