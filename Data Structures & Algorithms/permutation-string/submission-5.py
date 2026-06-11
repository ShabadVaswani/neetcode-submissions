class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashone = {}
        hashtwo = {}
        if len(s1) > len(s2): return False
        for i in range(len(s1)):
            hashone[s1[i]] = hashone.get(s1[i], 0) + 1
            hashtwo[s2[i]] = hashtwo.get(s2[i], 0) + 1
        l, r = 0, len(s1)-1
        if hashone == hashtwo:
            return True

        while r < len(s2)-1:
            print(hashone, hashtwo, l, r)
            r+=1
            hashtwo[s2[r]] = hashtwo.get(s2[r], 0) + 1
            hashtwo[s2[l]] = hashtwo.get(s2[l], 0) - 1
            if hashtwo[s2[l]] == 0:
                hashtwo.pop(s2[l])
            l+=1
            if hashone == hashtwo:
                return True
        return False