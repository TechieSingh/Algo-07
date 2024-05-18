class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.result = 0
        empty_squares = 1  # To count the starting square as well
        start_x = start_y = 0
        
        # Find the starting point and count all the empty squares
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 0:
                    empty_squares += 1
        
        # Depth First Search with backtracking
        def dfs(x, y, count):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1:
                return
            
            if grid[x][y] == 2:
                if count == empty_squares:
                    self.result += 1
                return
            
            # Mark the square as visited
            temp = grid[x][y]
            grid[x][y] = -1
            
            # Explore all four possible directions
            dfs(x + 1, y, count + 1)
            dfs(x - 1, y, count + 1)
            dfs(x, y + 1, count + 1)
            dfs(x, y - 1, count + 1)
            
            # Backtrack
            grid[x][y] = temp
        
        # Start DFS from the starting point
        dfs(start_x, start_y, 0)
        return self.result


        