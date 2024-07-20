class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = [[0] * len(colSum) for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                val = min(rowSum[i], colSum[j])
                res[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val


        return res        