class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        res = []

        def dfs(res, index):
            if index == len(nums):
                final.append(res.copy())
                return
            
            res.append(nums[index])
            dfs(res, index + 1)

            res.pop()
            dfs(res, index + 1)

        dfs(res, 0)
        print(final)
        return final