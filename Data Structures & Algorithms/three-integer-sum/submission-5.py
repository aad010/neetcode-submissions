class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputArray = []
        i = 0
        nums.sort()
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k] 
                if sum == 0:
                    sumArr = [nums[i], nums[j], nums[k]]
                    if sumArr not in outputArray:
                        outputArray.append(sumArr)
                    j += 1
                    k -= 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        
        return outputArray
        