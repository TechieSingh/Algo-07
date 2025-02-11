class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        a = list(s)
        l = len(part)
        i = 0
        while i <= len(a) - l:
            current_substring = ''.join(a[i:i+l])
            if current_substring == part:
                del a[i:i+l]
                i = max(0, i - l)
            else:
                i += 1
        return ''.join(a)