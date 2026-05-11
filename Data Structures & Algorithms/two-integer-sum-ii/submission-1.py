class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diff_dict = defaultdict(int)

        for i, v in enumerate(numbers):
            diff = target - v
            if diff in diff_dict:
                return [diff_dict[diff], i + 1]
            else:
                diff_dict[v] = i + 1
        
        return []