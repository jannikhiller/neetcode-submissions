import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        special_tokens = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        stack = []
        print(tokens)
        for token in tokens:
            print(stack, token)
            if token in special_tokens:
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(special_tokens[token](lhs, rhs))
            else:
                stack.append(int(token))
        return stack[0]


        