class Solution:
    def reverseWords(self, s: str) -> str:
        rstr=s[::-1]
        result=""
        words=rstr.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
            if i<len(words)-1:
                result+=words[i]+" "
            else:
                result+=words[i]
        return result
        