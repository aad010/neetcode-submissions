class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set() 

        for i in nums:
            if i in hs:
                return True
            hs.add(i)
        
        return False  



# UMPIRE
# Understand
# return true if any value appears > 1; else return false 
# ex: [1,2,3,3] => true because 3 appears twice

# Match
# Use set to track duplicates and iterate


# Plan
# set init
# for a number in nums 
#   check if number is in set
        # if yes then return true
    # otherwise add to set 
# return false if no duplicates