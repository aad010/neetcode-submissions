class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        else:
            stones_changed = [(-1 * i) for i in stones]
            heapq.heapify(stones_changed)
            while len(stones_changed) > 1:
                firstVal = heapq.heappop(stones_changed)
                secondVal = heapq.heappop(stones_changed)
                diff = max(firstVal, secondVal) - min(firstVal, secondVal)
                stones_changed.append(-1 * diff)
                heapq.heapify(stones_changed)
        if len(stones_changed) == 1:
            return -1 * stones_changed[0]
        else: 
            return 0