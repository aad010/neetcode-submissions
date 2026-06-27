class Solution:
    def rob(self, nums: List[int]) -> int:
        flag = True
        cacheZero = {}
        cacheOne = {}
        def dp(flag, i, cache):
            if i >= len(nums):
                return 0
            elif len(nums) > 1 and (flag is True) and (i == len(nums) - 1):
                return 0
            elif i in cache:
                return cache[i]
            else:
                cache[i] = max(nums[i] + dp(flag, i + 2, cache), dp(flag, i + 1, cache))
                return cache[i]

        return max(dp(True, 0, cacheZero), dp(False, 1, cacheOne))