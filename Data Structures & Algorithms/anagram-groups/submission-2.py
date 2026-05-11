class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            ["act","pots","tops","cat","stop","hat"]
            {"act": ["act"], "opst": ["pots", "tops"]}

        '''
        dictAnagrams = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in dictAnagrams.keys():
                dictAnagrams[sortedWord] = []
            dictAnagrams[sortedWord].append(word)

        values = list(dictAnagrams.values())
        return values
                