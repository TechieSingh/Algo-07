import operator

class Solution:
    def clumsy(self,N: int) -> int:
        if N == 0: return 0
        if N == 1: return 1
        if N == 2: return 2 * 1
        if N == 3: return 3 * 2 // 1
        stack = []
        stack.append(N)
        N -= 1
        stack.append(stack.pop() * N)
        N -= 1
        stack.append(stack.pop() // N)
        N -= 1
        operator = '+'
        
        while N > 0:
            if operator == '+':
                stack.append(N)
                operator = '-'
            elif operator == '-':
                stack.append(-N)
                operator = '*'
            elif operator == '*':
                stack.append(stack.pop() * N)
                operator = '/'
            elif operator == '/':
                top = stack.pop()
                if top < 0:
                    stack.append(-(abs(top) // N))
                else:
                    stack.append(top // N)
                operator = '+'
            N -= 1
        return sum(stack)




