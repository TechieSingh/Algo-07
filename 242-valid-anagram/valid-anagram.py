class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa=sorted(s)
        ta=sorted(t)
        if sa==ta:
            return True
        else:
            return False
        