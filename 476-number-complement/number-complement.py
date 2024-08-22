class Solution:
    def findComplement(self, num: int) -> int:
        s=bin(num)[2:]
        binary=""
        for i in range(len(s)):
            if s[i]=="0":
                binary+="1"
            else:
                binary+="0"
        return int(binary, 2)
        