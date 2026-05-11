class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for word in strs:
            encodedStr += str(len(word)) + "#" + word
        return encodedStr

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < (len(s)):
            j = i + 1
            while s[j] != '#':
                j += 1
            lenOfWord = s[i : j]
            res.append(s[j + 1 : j + 1 + int(lenOfWord)])
            i = j + 1 + int(lenOfWord)
        return res
            
