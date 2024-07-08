class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        index = 0  
        print(arr)
        
        while len(arr) > 1:
            index = (index + k - 1) % len(arr)  
            arr.pop(index)
            print(arr)
        
        return arr[0]