class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for word in strs: 
            sorted_word = "".join(sorted(word))
            hm[sorted_word].append(word)

        return [i for i in hm.values()]