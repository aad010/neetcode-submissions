import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)
        minHours = -1

        def feasible(limit):
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / limit)
            return hours <= h

        while left <= right:
            middle = (left + right) // 2
            if feasible(middle):
                right = middle - 1
                minHours = middle
            else:
                left = middle + 1
        
        return minHours
