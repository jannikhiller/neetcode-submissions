class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        stack = [ "(" ]
        while stack:
            string = stack.pop()
            left_parens = string.count("(")
            right_parens = string.count(")")

            if len(string) == 2*n:
                out.append(string)
                continue

            if left_parens < n:
                stack.append(string + "(")
            if left_parens - right_parens > 0:
                stack.append(string + ")")
        
        return out