class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        # Step 1: Compute prefix XOR array
        prefixXOR = [0] * (n + 1)
        for i in range(n):
            prefixXOR[i + 1] = prefixXOR[i] ^ arr[i]
        
        # Step 2: Answer queries using prefix XOR
        result = []
        for L, R in queries:
            xor_result = prefixXOR[R + 1] ^ prefixXOR[L]
            result.append(xor_result)
        
        # Step 3: Return the result
        return result
