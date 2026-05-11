class TrieNode:
    def __init__(self):
        self.eow = False 
        self.neighbors = {}


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for l in word:
            if l not in curr.neighbors:
                curr.neighbors[l] = TrieNode()
            curr = curr.neighbors[l]
        curr.eow = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s in curr.neighbors:
                curr = curr.neighbors[s]
            else:
                return False
        
        return curr.eow

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            if s in curr.neighbors:
                curr = curr.neighbors[s]
            else:
                return False
        
        return True
        
        