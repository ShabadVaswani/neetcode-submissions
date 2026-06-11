class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        d1 = dict()
        if len(s) != len(t):
            return False
        for i in list(s):
            if i in d.keys():
                d[i]+=1
            else:
                d[i] =1
        for i in list(t):
            if i in d1.keys():
                d1[i]+=1
            else:
                d1[i] =1
        if len(d.keys())!=len(d1.keys()):
            return False
        for i in d1.keys():
            if i not in d.keys():
                return False
            if d1[i] != d[i]:
                return False
        return True