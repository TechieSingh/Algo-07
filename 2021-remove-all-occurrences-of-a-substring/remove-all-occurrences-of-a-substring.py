class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result=s
        m=len(part)
        while part in result:
            result = result.replace(part, '',1)
        return result

        