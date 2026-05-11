class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        given array of distinct integers (nums) and target 
        goal is to return list of all unique combinations of nums
        where the chosen numbers sum to target 

        '''
        result = []

        def backtrack(total, comboArr, index):
            if total == target:
                result.append(comboArr.copy())
                return
            elif total > target or index == len(nums):
                return 
            
            comboArr.append(nums[index])
            backtrack(total + nums[index], comboArr, index)
            comboArr.pop()
            backtrack(total, comboArr, index + 1)
        
        backtrack(0, [], 0)
        return result
            
