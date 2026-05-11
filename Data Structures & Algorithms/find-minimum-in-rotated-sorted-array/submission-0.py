class Solution:
    def findMin(self, nums: List[int]) -> int:
        ''' 
            goal: given array of length n that is sorted 
            in ascending order
            [3,4,5,6,1,2]
            l    m     r  


        '''
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[right] < nums[left]:
                left += 1
            elif nums[right] > nums[left]:
                right -= 1
            else:
                return nums[middle]