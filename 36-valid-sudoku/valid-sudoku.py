class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for k in range(81):
            i, j = divmod(k, 9)
            c = board[i][j]
            if c != '.':
                if (c, i) in seen or (j, c) in seen or (i // 3, j // 3, c) in seen:
                    return False
                seen.add((c, i))
                seen.add((j, c))
                seen.add((i // 3, j // 3, c))
        return True
        