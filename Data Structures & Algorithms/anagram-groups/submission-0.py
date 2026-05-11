class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for i in strs: 
            sortedI = "".join(sorted(i))
            print(sortedI)

            
            if sortedI in anagrams:
                anagrams[sortedI].append(i)
            else:
                anagrams[sortedI] = []
                anagrams[sortedI].append(i)
        return(list(anagrams.values()))
        

        