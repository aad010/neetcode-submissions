class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstStrDict = defaultdict(int)

        for letter in s:
            firstStrDict[letter] += 1

        for letter in t:
            if firstStrDict[letter] <= 0:
                return False
            else:
                firstStrDict[letter] -= 1
            
        vals = set(firstStrDict.values())

        return True if (len(vals) == 1 and 0 in vals) else False