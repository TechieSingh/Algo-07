class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        my_dict = dict(zip(heights, names))

        sorted_items = sorted(my_dict.items(), key=lambda x: x[0], reverse=True)

        result = [name for height, name in sorted_items]
        return result


        