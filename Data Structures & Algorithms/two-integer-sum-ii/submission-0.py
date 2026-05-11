class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ''' 
            Goal: return indices of 2 numbers in an array that add up 
            to a target and index1 must be less than index2.

            ex: [1,2,3,4] target = 3
                l  r

        '''
        leftPtr = 0 
        rightPtr = len(numbers) - 1

        while True: 
            leftVal = numbers[leftPtr]
            rightVal = numbers[rightPtr]
            totalSum = leftVal + rightVal

            if totalSum > target:
                rightPtr -= 1
            elif totalSum < target:
                leftPtr += 1
            else:
                return [leftPtr + 1, rightPtr + 1]