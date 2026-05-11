class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {"]":"[", "}": "{", ")":"("}

        for l in s:
            if l in parens:
                if stack and (stack[-1] == parens[l]):
                    stack.pop()
                else:
                    stack.append(l)
            else:
                stack.append(l)
        
        return True if len(stack) == 0 else False