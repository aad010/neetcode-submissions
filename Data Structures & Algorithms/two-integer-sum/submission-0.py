'''
Understand: 
    we have an array of ints called nums and target (an int)
    goal is to return indices i and j such that nums[i] + nums[j] == target AND the indices are not the same

    every input has one valid pair of indices and we return the smaller index first


Match: 
    Use a hashmap and iterate through array

Plan: 
    init hm
    iterate through nums
        get difference
        if difference in hm
            return index of difference and curr_index
        else add difference to hm
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}


        for i, v in enumerate(nums):
            diff = target - v 
            if diff in hm:
                return [hm[diff],i]
            hm[v] = i