class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            return kth largest element in array given an unsorted array of integers (nums) and k

            [2,3,1,5,4], k = 2

            -5
           -4 -3
         -2 -1
        pop 5
        k = 1
        pop 4
        k = 0
        return abs(-4)
        '''
        nums = [-val for val in nums]
        heapq.heapify(nums)
        val = 0
        while k > 0:
            val = heapq.heappop(nums)
            k -= 1
        if val < 0:
            return abs(val)
        else:
            return -val