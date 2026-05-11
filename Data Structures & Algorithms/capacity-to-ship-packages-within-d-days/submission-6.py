class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        minWeight = -1

        while left <= right:
            middle = (left + right) // 2
            if self.feasible(days, middle, weights):
                minWeight = middle 
                right = middle - 1
            else:
                left = middle + 1
        
        return minWeight

    def feasible(self, days, limit, weights):
        currSum = 0
        totalDays = 1
        print(limit, "s")
        for i in weights:
            currSum += i
            if currSum > limit:
                currSum = i
                totalDays += 1

        print("days", totalDays)
        print(totalDays)
        return totalDays <= days