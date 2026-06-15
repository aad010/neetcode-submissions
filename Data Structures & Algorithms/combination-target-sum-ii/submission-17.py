class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        final = []
        res = []

        def dfs(res, index, total):
            if total == target:
                final.append(res.copy())
                return
            
            if total > target or index == len(candidates):
                return 

            # choose candidates[index]
            res.append(candidates[index])
            dfs(res, index + 1, total + candidates[index])
            res.pop()

            # skip duplicates when NOT choosing candidates[index]
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            # don't choose candidates[index]
            dfs(res, index + 1, total)

        dfs(res, 0, 0)
        return final