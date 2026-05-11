class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPtr = 0
        charCtr = set()
        counter = 0
        maxCtr = 0 

        for i in range(len(s)):
            while s[i] in charCtr:
                charCtr.remove(s[leftPtr])
                leftPtr += 1
                counter -= 1
            
            charCtr.add(s[i])
            counter += 1
            maxCtr = max(maxCtr, counter)
        return maxCtr
