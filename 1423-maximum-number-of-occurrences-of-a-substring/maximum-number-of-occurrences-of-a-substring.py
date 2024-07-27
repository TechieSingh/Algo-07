from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        n = len(s)
        substring_count = defaultdict(int)
        
        for size in range(minSize, maxSize + 1):
            for i in range(n-size+1):
                substring = s[i:i + size]
                if len(set(substring)) <= maxLetters:
                    substring_count[substring] += 1
        
        return max(substring_count.values(), default=0)