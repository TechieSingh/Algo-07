class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        sol=2
        if sol==1:
            res = [[0] * len(colSum) for _ in range(len(rowSum))]
            for i in range(len(rowSum)):
                for j in range(len(colSum)):
                    val = min(rowSum[i], colSum[j])
                    res[i][j] = val
                    rowSum[i] -= val
                    colSum[j] -= val
            return res 


        if sol==2:
            col_sum = colSum
            row_sum = rowSum
            
            mat = [[0]*len(col_sum) for i in range(len(row_sum))]
            i = 0
            j = 0
            while i < len(row_sum) and j < len(col_sum):
                mat[i][j] = min(row_sum[i], col_sum[j])
                if row_sum[i] == col_sum[j]:
                    i += 1
                    j += 1
                elif row_sum[i] > col_sum[j]:
                    row_sum[i] -= col_sum[j]
                    j += 1
                else:
                    col_sum[j] -= row_sum[i]
                    i += 1

            return mat