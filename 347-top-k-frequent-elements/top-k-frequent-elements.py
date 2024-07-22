class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        hash_map = Counter(nums)
        
        sorted_items = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            result.append(sorted_items[i][0])


        return result
        