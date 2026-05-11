class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictOne = {}
        dictTwo = {}
        
        if len(s) != len(t):
            return False

        for letter in s:
            if letter not in dictOne:
                dictOne[letter] = 1
            else:
                dictOne[letter] = dictOne[letter] + 1
        

        for letter in t:
            if letter not in dictTwo:
                dictTwo[letter] = 1
            else:
                dictTwo[letter] = dictTwo[letter] + 1
        
        print(dictOne)
        print(dictTwo)

        for letter in dictOne.keys():
            if letter not in dictTwo:
                return False
            elif dictOne[letter] != dictTwo[letter]:
                return False
        
        return True
        