class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final = []
        res = []

        def dfs(res, index, total):
            if total == target:
                final.append(res.copy())
                return
            elif total > target or index == len(nums):
                return
            else:
                res.append(nums[index])
                dfs(res, index, total + nums[index])

                res.pop()
                dfs(res, index + 1, total)
        
        dfs(res, 0, 0)
        print(final)
        return final