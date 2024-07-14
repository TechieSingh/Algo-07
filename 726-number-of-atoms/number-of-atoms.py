from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        map = defaultdict(int)
        i = 0
        n = len(formula)
        while i < n:
            c = formula[i]        
            i += 1
            if c == '(':
                stack.append(map)
                map = defaultdict(int)
            elif c == ')':
                val = 0
                while i < n and formula[i].isdigit():
                    val = val * 10 + ord(formula[i]) - ord("0")
                    i += 1
                if val == 0:
                    val = 1
                if stack:
                    temp = map
                    map = stack.pop()
                    for k, v in temp.items():
                        if k in map:
                            map[k] += temp[k] * val
                        else:
                            map[k] = temp[k] * val

            else:
                start = i - 1
                while i < n and formula[i].islower():
                    i += 1

                s = formula[start: i]
                val = 0
                while i < n and formula[i].isdigit():
                    val = val * 10 + ord(formula[i]) - ord('0')
                    i += 1
                
                if val == 0:
                    val = 1

                map[s] += val

        result = ""
        for key in sorted(map):
            result += key
            if map[key] > 1:
                result += str(map[key])

        return result


    

        