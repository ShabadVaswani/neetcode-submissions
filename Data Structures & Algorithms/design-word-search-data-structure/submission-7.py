class TrieNode:
    def __init__(self):
        self.next = {}
        self.endofword = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char not in temp.next:
                temp.next[char] = TrieNode()
            temp = temp.next[char]

        temp.endofword = True

    def search(self, word: str) -> bool:
        
        temp = self.root                    
        def dfs(index, temp):
            
            for i in range(index, len(word)):
                if word[i] == '.':
                    for k in temp.next.values():
                        if dfs(i+1, k):
                            return True
                    return False
                else: 
                    if word[i] not in temp.next:
                        return False
                    temp = temp.next[word[i]]
            return temp.endofword

        
        return dfs(0,temp)
