class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs: 
            s += str(len(word)) + "#" + word
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        listOfWords = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            number = int(''.join(s[i:j]))
            word = s[j + 1: (j + 1) + number]
            listOfWords.append(word)
            i = (j + 1) + number

        print(listOfWords)
        return listOfWords
