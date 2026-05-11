class KthLargest:
    '''
        design class to find kth largest integer in a stream of values
        including dupes

        ex: [1,2,3,3] 2nd largest is k = 2 is 3

        init object given an int k and nums
    '''

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        