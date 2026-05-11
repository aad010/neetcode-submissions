class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for oneString in strs:
            encodedString += str(len(oneString)) + "#" + oneString
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedList = []

        index = 0
        while index < len(s):
            counter = ""
            while s[index] != '#':
                counter += str(s[index])
                index += 1
            intCounter = int(counter)
            index += 1
            word = s[index: index + intCounter]
            decodedList.append(word)
            index += intCounter
        return decodedList
