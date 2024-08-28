# (1) Use separate for loops to go through the rows, columns, and each 3x3 grid. Create a new set for each one to check for any duplicate values => O(9^2) = O(1) time complexity because we have a fixed 9x9 sudoku board. 
# (2) Use one set of for loops and a unique HashSet for the rows, columns, and 3x3 grids. Check for any duplicates => O(9^2) = O(1) time complexity because we have a fixed 9x9 sudoku board.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # row : [values]
        cols = defaultdict(set) # col : [values]
        grids = defaultdict(set) # (row // 3, col // 3) : [values]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if (board[r][c] in rows[r] or 
                        board[r][c] in cols[c] or 
                        board[r][c] in grids[(r // 3, c // 3)]):
                        return False
                    
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    # store element in the correct grid using a tuple key
                    grids[(r // 3, c // 3)].add(board[r][c])
                    
        return True