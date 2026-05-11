class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                triplet = nums[i] + nums[j] + nums[k]
                if triplet == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -= 1
                    while j < len(nums) and nums[j - 1] == nums[j]: 
                        j += 1
                        print(j)
                    while k >= 0 and nums[k] == nums[k + 1]:
                        k -= 1
                elif triplet > 0:
                    k -= 1
                    while k >= 0 and nums[k] == nums[(k + 1)]:
                        k -= 1
                else:
                    j += 1
                    while j < len(nums) and nums[j] == nums[(j - 1)]:
                        j += 1
        return res
                