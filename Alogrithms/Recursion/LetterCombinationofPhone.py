from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        my_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, path: str):
            # Base case: if the current path is equal to the length of digits, add the path to the result
            if index == len(digits):
                result.append(path)
                return
            
            # Get the current digit and the corresponding letters from the dictionary
            current_digit = digits[index]
            for letter in my_dict[current_digit]:
                backtrack(index + 1, path + letter)
        
        # Initiate the backtracking process from the first digit
        backtrack(0, "")
        return result

# Example usage
sol = Solution()
print(sol.letterCombinations("23"))
