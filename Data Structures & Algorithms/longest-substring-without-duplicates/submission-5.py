class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setOfLetters = set()
        left = 0
        right = 0
        maxLength = 0

        while right < len(s):
            while s[right] in setOfLetters:
                setOfLetters.remove(s[left])
                left += 1

            setOfLetters.add(s[right])
            maxLength = max(right - left + 1, maxLength)
            right += 1
            
        return maxLength
                    