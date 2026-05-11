class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in hm:
                return [hm[diff], i]
            else:
                hm[v] = i
        
        return []