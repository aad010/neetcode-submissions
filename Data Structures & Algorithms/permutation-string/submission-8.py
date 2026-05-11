class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        rightPtr = 0
        res = ""

        s1StringList = sorted(s1)
        s1StringSorted = "".join(s1StringList)
        
        while rightPtr < len(s2):
            leftPtr = rightPtr
            while leftPtr < len(s2) and s2[leftPtr] in s1:
                res += s2[leftPtr]
                leftPtr += 1
                if len(res) == len(s1):
                    break 
            if len(res) > 0:
                resStringList = sorted(res)
                resStringSorted = "".join(resStringList)
                if s1StringSorted == resStringSorted and len(res):
                    return True 

            res = ""
            rightPtr += 1
        
        return False
            