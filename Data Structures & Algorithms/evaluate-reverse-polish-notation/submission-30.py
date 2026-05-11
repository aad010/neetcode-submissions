class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for op in tokens:
            if op not in operators:
                stack.append(int(op))
            else:
                num = 0
                if op == "+":
                    first_num = stack.pop()                          
                    second_num = stack.pop()     
                    num = first_num + second_num                     
                elif op == "-":
                    first_num = stack.pop()
                    second_num = stack.pop()
                    num = second_num - first_num
                elif op == "*":
                    first_num = stack.pop()                          
                    second_num = stack.pop()     
                    num = first_num * second_num  
                elif op == "/": 
                    print("HI")
                    first_num = stack.pop()
                    second_num = stack.pop()
                    print(first_num)
                    print(second_num)
                    num = int(second_num / first_num)
                    print(num)
                stack.append(num)
                print(stack)
        return stack[-1]
                            