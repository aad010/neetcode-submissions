class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}':'{',')':'(',']':'['}
        stack = []
        for letter in s:
            if letter in brackets and len(stack) > 0:
                if stack[-1] == brackets[letter]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)

        return True if len(stack) == 0 else False