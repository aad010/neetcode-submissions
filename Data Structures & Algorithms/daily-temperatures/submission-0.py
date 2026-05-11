class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            we are given temperatures (an array with index i representing temperature on ith day)
            goal is to make and return result where index i is num of days after ith day before warmer temp appears on future day
            if no day appears then put result[i] to 0

            ex: 
            [30,38,30,36,35,40,28]

            result = [1,4,1,2,1,0,0]
            [1,]
            stack=[[38:1],[36:2]]
        '''
        stack = []
        result = [0] * len(temperatures)

        for i,v in enumerate(temperatures): 
            while stack and stack[len(stack) - 1][0] < v: 
                value = stack.pop()
                result[value[1]] = i - value[1]
            stack.append([v,i])

        return result
        