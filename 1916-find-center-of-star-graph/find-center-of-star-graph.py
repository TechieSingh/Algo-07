class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        my_dict={}
        for row in edges:
            for element in row:
                if element in my_dict:
                    my_dict[element] += 1
                else:
                    my_dict[element] = 1

        higest_count= max(my_dict,key=my_dict.get)
        return higest_count
                
        