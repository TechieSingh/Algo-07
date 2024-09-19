class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results=[]
        if len(expression)==0:
            return results
        if len(expression)==1:
            return [int(expression)]
        if len(expression)==2 and expression[0].isdigit():
            return [int(expression)]
        for i,current_char in enumerate(expression):
            if current_char.isdigit():
                continue
            left_results=self.diffWaysToCompute(expression[:i])
            right_results=self.diffWaysToCompute(expression[i+1:])
            for left_val in left_results:
                for right_val in right_results:
                    if current_char == "+":
                        results.append(left_val + right_val)
                    elif current_char == "-":
                        results.append(left_val - right_val)
                    elif current_char == "*":
                        results.append(left_val * right_val)

        return results

        