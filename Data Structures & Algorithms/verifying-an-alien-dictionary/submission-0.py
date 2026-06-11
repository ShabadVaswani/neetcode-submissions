class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderdict = {}
        for i, char in enumerate(order):
            orderdict[char] = i

        for i in range(len(words)-1):
            curr = words[i]
            nxt = words[i+1]
            flag = True
            for j in range(min(len(words[i]), len(words[i+1]))):
                print()
                if orderdict[curr[j]] > orderdict[nxt[j]]:
                    return False
                if orderdict[curr[j]] < orderdict[nxt[j]]:
                    flag = False
                    break
            if flag and len(curr) > len(nxt):
                return False
        return True


