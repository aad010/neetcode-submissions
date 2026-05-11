class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0

        maxVal = 0
        setOfChars = set()
        for r in range(len(s)):
            while s[r] in setOfChars:
                setOfChars.remove(s[l])
                l += 1
            setOfChars.add(s[r])
            maxVal = max(maxVal, (r - l) + 1)
    
        return maxVal