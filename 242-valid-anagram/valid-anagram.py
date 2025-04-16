class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa=list(s)
        ta=list(t)
        sa=sorted(sa)
        ta=sorted(ta)
        if sa==ta:
            return True
        else:
            return False
        