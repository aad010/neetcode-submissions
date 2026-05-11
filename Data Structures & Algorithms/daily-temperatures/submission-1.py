class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                temp_val = stack[-1][0]
                temp_idx = stack[-1][1]
                res[temp_idx] = i - temp_idx
                stack.pop()
            stack.append((temp, i))
        
        return res