class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        table={}

        for each in strs:
            key=''.join(sorted(each))
            if key not in table:
                table[key]=[]
            table[key].append(each)
        for value in table.values():
            result.append(value)
        return result
        