class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            Goal: given a string "s" that has only uppercase english characters
            and an integer "k" 
            we can choose up to "k" characters of a string and replace them with any other 
            uppercase English character 
            
            after performing AT MOST k replcacements replace length of longest string which contains only one distinct char


            EX:
            s = "XYYX", k = 2
            XYYX
            0123
            {X:1, Y: 2}
            What to do:
            we can use a set

            {X}
            {X,Y} => can replace Y with x
            {X,Y} => Y already in set and set count > 2 so can replace Y with x (atp k = 2)


            {A: 2}            
        '''
        left = 0 
        longestLength = 0
        maxOccurrences = 0
        charDict = {}
        result = 0

        for right in range(len(s)):
            charDict[s[right]] = charDict.get(s[right],0) + 1
            maxOccurrences = max(charDict[s[right]], maxOccurrences)

            while ((right - left + 1) - maxOccurrences) > k:
                charDict[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        
        return result

        