class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        combined_arr = zip(position, speed)
        sorted_arr = sorted(combined_arr)
        print(sorted_arr)
        for pos, speed in sorted_arr[::-1]:
            remaining_steps = (target - pos) / speed
            if stack and stack[-1] >= remaining_steps:
                continue 
            else:
                stack.append(remaining_steps)
        
        return len(stack)