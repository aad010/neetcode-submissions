class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            goal: we are given an array of strings
            the goal is to group all anagrams together into sublists and return the output in any order


            ex:
            ["act","pots","tops","cat","stop","hat"] = input
            output = [[act,'cat],[ptos,tops,stop],[hat]]
        
            iterate through each word in string
            count characters and store in array (ord(letter) - ord('a'))

        '''
        result = defaultdict(list)

        for word in strs: 
            letterCount = [0 for i in range(26)]
            for letter in word: 
                letterCount[ord(letter) - ord('a')] += 1
            result[tuple(letterCount)].append(word)
        
        return result.values()
        