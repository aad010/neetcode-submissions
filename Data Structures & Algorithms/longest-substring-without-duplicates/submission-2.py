class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''' 
        goal: we are given string s and goal is to find longest
        substring without duplicate characters

        ex: s="zxyzxyz"
            {z,x,y}    
        
        '''
        duplicateSet = set()
        result = 0
        left = 0

        for right in range(0, len(s)):
            while s[right] in duplicateSet:
                duplicateSet.remove(s[left])
                left += 1
            duplicateSet.add(s[right])
            result = max(result, right - left + 1)
        return result

        