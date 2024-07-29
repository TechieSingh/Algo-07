class Solution:
    def numTeams(self, rating: List[int]) -> int:
        hash_map_up={}
        hash_map_down={}
        n = len(rating)
        count = 0
        for i in range(n):
            hash_map_up[i]=[]
            hash_map_down[i]=[]
            for j in range(i+1,n):
                if rating[j]>rating[i]:
                    hash_map_up[i].append(j)
                elif rating[j]<rating[i]:
                    hash_map_down[i].append(j)
        for i in range(n):
            for index in hash_map_up[i]:
                count+= len(hash_map_up[index])
            for index in hash_map_down[i]:
                count+= len(hash_map_down[index])

        return count
        