class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            given array of distinct ints (nums) sroted in asceding order
            and target 
            goal is to search target within nums in O(log n)!


            [-1,0,2,4,6,8], target = -2
                    l   r
            start from middle
            if target > middle:
                look to right
            else: look to left
        '''
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1 