class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa=sorted(s)
        ta=sorted(t)
        return sa==ta
        