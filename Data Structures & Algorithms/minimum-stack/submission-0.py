class MinStack:
    def __init__(self):
        self.stack = []    
        self.minVal = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minVal > val:
            self.minVal = val

    def pop(self) -> None:
        self.stack.pop(len(self.stack) - 1)
        self.minVal = float("inf")
        for i in self.stack:
            if i < self.minVal:
                self.minVal = i

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minVal

        
