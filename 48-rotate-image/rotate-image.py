class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        result=[]
        row=len(matrix)
        col=len(matrix[0])

        for i in range(col):
            new_row = []
            for j in range(row-1,-1,-1):
                new_row.append(matrix[j][i])
            result.append(new_row)
        
        for i in range(row):
            for j in range(col):
                matrix[i][j] = result[i][j]


        