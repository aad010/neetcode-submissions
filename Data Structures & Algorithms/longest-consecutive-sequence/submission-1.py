class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            given array nums, return length of longest consecutive sequence of elements
            ex: [2,20,4,10,3,4,5]
            longest is 2,3,4,5

            (2,20,4,10,3,5)

            look at 2:
            see if 3 there yes
            then 4 yes
            5 yes
            length is 4!
            then go to 20: just 1
            then 4: just 2

            code:
            convert arr to set
            longestLength = 1
            iterate through elements in arr
                if num - 1 not in set:
                    length = 1
                    while (num + length in set):
                        length += 1
                    longestLength = longestLength(length, longestLength)
            return longestLength
        '''
        if nums == []:
            return 0
        
        numbersInArr = set(nums)
        
        longestLength = 1
        for val in nums:
            if (val - 1) not in numbersInArr:
                length = 1
                while (val + length) in numbersInArr:
                    length += 1
                longestLength = max(length, longestLength)
        return longestLength
        