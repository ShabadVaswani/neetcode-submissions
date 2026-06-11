class TrieNode:
    def __init__(self):
        self.next = {}
        self.endofword = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        
        for i in range(len(word)):
            if word[i] not in temp.next:
                temp.next[word[i]] = TrieNode()
            temp = temp.next[word[i]]
            if i == len(word) - 1:
                temp.endofword = True




    def search(self, word: str) -> bool:
        temp = self.root

        for char in word:
            if char in temp.next:
                temp = temp.next[char]
                continue
            else:
                return False         
        return temp.endofword       


    def startsWith(self, prefix: str) -> bool:

        temp = self.root

        for char in prefix:
            if char in temp.next:
                temp = temp.next[char]
                continue
            else:
                return False
        return True
        
        