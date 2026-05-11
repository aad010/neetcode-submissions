class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPtr = 0
        dupsSet = set()
        maxRes = 0
        for rightPtr in range(0, len(s)):
            while s[rightPtr] in dupsSet:
                dupsSet.remove(s[leftPtr])
                leftPtr += 1
            dupsSet.add(s[rightPtr])
            maxRes = max(maxRes, rightPtr - leftPtr + 1)
        
        return maxRes