'''
Understand:
    if 2 strings are anagrams of each other return true; else false 
    anagram: contains exact same characters as another string but order can be diff!
    length of both strings have to be the same!
Match: 
    use hashmap to store letter counts
    and iterate through strings 

Plan:
    check length is same!

    hs for first string
    hs for second string
    iterate through first string and store letter count in hmap
    iterate through second string and store letter count in hmap
    
    and then iterate through one hmap
        for each letter compare count to count in other hmap
            if not the same then return false

    return true 
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHMAP = {}
        tHMAP = {}

        if len(s) != len(t):
            return False

        for i in s:
            sHMAP[i] = sHMAP.get(i, 0) + 1
        for i in t:
            tHMAP[i] = tHMAP.get(i, 0) + 1 

        for k,v in tHMAP.items():
            if k not in sHMAP or sHMAP.get(k) != v:
                return False 

        return True