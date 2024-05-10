class Solution:
    def ispossible(self, position: List[int], mid:int, m:int)-> bool:
        ball_count=1
        last_position = position[0]
        for i in range(1, len(position)):
            if position[i]-last_position>=mid:
                ball_count+=1
                last_position=position[i]
                if ball_count==m:
                    return True

        return False


    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low=1
        high=position[-1] - position[0]
        result=low
        while(low<=high):
            mid=(low+high)//2
            if self.ispossible(position,mid,m):
                result=mid
                low=mid+1
            else:
                high=mid-1
        return result

            

        

        
        