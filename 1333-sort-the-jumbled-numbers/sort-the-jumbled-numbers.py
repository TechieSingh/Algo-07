
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_values = []
        
        # Create mapped values using the mapping
        for num in nums:
            mapped_num = int("".join(str(mapping[int(digit)]) for digit in str(num)))
            mapped_values.append((num, mapped_num))
        
        # Sort the mapped values based on the mapped number
        mapped_values.sort(key=lambda x: x[1])
        
        # Extract the original numbers in the new order
        result = [num for num, _ in mapped_values]
        
        return result