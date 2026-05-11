class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ''' 
            nums=[1,2,4,6]
        '''
        prefixProduct = []
        prefixProduct.append(nums[0])
        for i in range(1, len(nums)):
            prefixProduct.append(prefixProduct[i - 1] * nums[i])
        print(prefixProduct)

        postfixProduct = [0] * len(nums)
        postfixProduct[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            print(nums[i])
            postfixProduct[i] = postfixProduct[i + 1] * nums[i]

        print(postfixProduct)
        resultArr = [0] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                resultArr[i] = postfixProduct[1]
            elif i == len(nums) - 1:
                resultArr[i] = prefixProduct[len(nums) - 2]
            else:
                resultArr[i] = prefixProduct[i - 1] * postfixProduct[i + 1]

        return resultArr

        