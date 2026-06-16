class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False 


class PrefixTree:
    def __init__(self):
        self.trie = TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.trie
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for s in word:
            if s not in curr.children:
                return False
            else:
                curr = curr.children[s]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for s in prefix:
            if s not in curr.children:
                return False
            else:
                curr = curr.children[s]
        return True
            
        