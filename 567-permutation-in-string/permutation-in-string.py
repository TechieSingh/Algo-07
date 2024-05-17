class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        s1_count=[0]*26
        s2_count=[0]*26

        for i in range(n):
            s1_count[ord(s1[i])-ord("a")]+=1
            s2_count[ord(s2[i])-ord("a")]+=1
        
        if s1_count==s2_count:
            return True
        
        for j in range(n,m):
            s2_count[ord(s2[j])-ord("a")]+=1
            s2_count[ord(s2[j-n])-ord("a")]-=1

            if s1_count==s2_count:
                return True

        return False



            