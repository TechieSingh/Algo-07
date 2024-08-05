class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        result=""
        count = Counter(arr)
        distinct = [x for x in arr if count[x] == 1]
        if k<= len(distinct):
            return distinct[k-1]
        return result
        