class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            given two strings s1 and s2
            if s2 contains permutation of s1 return true else false
            ex: s1 = abc, s2 = lecabee abc in s2 as cab
            s2 = lecabee

            leca

        '''

        left = 0
        theString = []
        for right in range(len(s2)):
            while (right - left + 1) > len(s1):
                theString.pop(0)
                left += 1
            theString.append(s2[right])
            word = "".join(theString)
            if sorted(word) == sorted(s1):
                return True
        return False