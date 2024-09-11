class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_result = start ^ goal
        count= bin(xor_result).count('1')
        return count

        