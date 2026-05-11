class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            [3,4,5,6], target = 7
            {3: 0}
        '''
        numbersHashDict = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference not in numbersHashDict.keys():
                numbersHashDict[value] = index
            else:
                return [numbersHashDict[difference], index]

        return [] 