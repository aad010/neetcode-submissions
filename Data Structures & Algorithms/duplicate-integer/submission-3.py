class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setChecker = set()

        for num in nums:
            if num not in setChecker:
                setChecker.add(num)
            else:
                return True
        
        return False