class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
            given array of strings "tokens" that reps valid arithmetic expr
            operands may be ints or results of other operations
            operators = +,-,*,/

        understand ex:
        [1,2,+,3,*,4,-] = 

        [1,2] encounter + so pop 2 and 1 and then add sum back to stack
        [3,3] encounter * so pop 3 and 3 and * then add back to stack
        [9,4] encounter - so pop 4 and 9 and then 9 - 4 and add back to stack
        [5]
        '''
        resultStack = []

        for val in tokens:
            if val == "+":
                secondVal = resultStack.pop()
                firstVal = resultStack.pop()
                sumOfVals = firstVal + secondVal
                resultStack.append(sumOfVals)
            elif val == "-":
                secondVal = resultStack.pop()
                firstVal = resultStack.pop()
                subOfVals = firstVal - secondVal
                resultStack.append(subOfVals)
            elif val == "*":
                secondVal = resultStack.pop()
                firstVal = resultStack.pop()
                multOfVals = firstVal * secondVal
                resultStack.append(multOfVals)
            elif val == "/":
                secondVal = resultStack.pop()
                firstVal = resultStack.pop()
                divOfVals = int(firstVal / secondVal)
                resultStack.append(divOfVals)
            else:
                resultStack.append(int(val))
            print(resultStack)
        return resultStack[0]
