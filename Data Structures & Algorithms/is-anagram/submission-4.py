class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = {}, {}

        sList = [*s]
        tList = [*t]

        if len(sList)!=len(tList):
            return False
        for i in sList:
            s1[i] = 1 + s1.get(i,0)
        for i in tList:
            t1[i] = 1 + t1.get(i,0)

        for i in sList:
            if s1[i] != t1.get(i, -1):
                return False
        return True
