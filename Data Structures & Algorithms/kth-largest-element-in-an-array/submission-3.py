class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxNums = []

        for num in nums:
            heapq.heappush(maxNums, -num)

        while k > 0:
            val = heapq.heappop(maxNums)
            k -= 1

        return val * -1
        