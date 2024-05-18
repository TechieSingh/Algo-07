from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        result = []
        n = len(chars)
        while i < n:
            result.append(chars[i])
            count = 1
            j = i + 1
            while j < n and chars[i] == chars[j]:
                count += 1
                j += 1
            if count > 1:
                for digit in str(count):
                    result.append(digit)
            i = j
        chars[:] = result
        return len(chars)

                    



        