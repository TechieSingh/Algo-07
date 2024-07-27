class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result=s
        while part in result:
            result = result.replace(part, '',1)
        return result

        