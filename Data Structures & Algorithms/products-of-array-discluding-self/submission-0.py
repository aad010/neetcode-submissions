class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        goal: given nums, return 'output' where output[i] is 
        product of all elements of nums except nums[i]

        ex: 
        [1,2,4,6]

        [48,24,12,8]

        prefix = [1,2,8,48]
        postfix = [48,48,24,6]
        output = prefix[0] = 1
                 postfix[0] = 48
        '''
        result = [1] * (len(nums))

        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result