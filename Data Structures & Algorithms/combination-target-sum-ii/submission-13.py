class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ''' 
            given array of ints (candidates that may contain duplicates) and target
            goal is to return list of all nique combos of candidates where chosen numbers
            sum to target

        '''
        result = []
        candidates.sort()
        def backtrack(combosList, total, index):
            if total == target:
                result.append(combosList.copy())
                return
            elif total > target or index == len(candidates):
                return 

            combosList.append(candidates[index])
            backtrack(combosList, total + candidates[index], index + 1)
            combosList.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(combosList, total, index + 1)
        
        backtrack([], 0, 0)
        return result