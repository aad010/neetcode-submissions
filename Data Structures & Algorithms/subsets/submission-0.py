class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        valuesList = []

        def dfs(index):
            if index == len(nums):
                result.append(valuesList.copy())
                return 
            
            valuesList.append(nums[index])
            dfs(index + 1)
            valuesList.pop()
            dfs(index + 1)

        dfs(0)
        return result