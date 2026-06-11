class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        patternmap = collections.defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                currpattern = word[:j] + '*' + word[j+1:]
                patternmap[currpattern].append(word)

        q = deque()

        q.append(beginWord)

        visited = set([beginWord])


        steps = 1

        while q:
            for i in range(len(q)):
                currword = q.popleft()
                print(currword)
                if currword == endWord:
                    return steps
                
                for j in range(len(currword)):
                    currpattern = currword[:j] + '*' + currword[j+1:]
                    for wordfound in patternmap[currpattern]:
                        if wordfound not in visited:
                            q.append(wordfound)
                            visited.add(wordfound)

            steps += 1
                


        return 0
