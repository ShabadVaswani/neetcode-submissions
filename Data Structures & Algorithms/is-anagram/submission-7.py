class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        d1 = dict()
        if len(s) != len(t):
            return False
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i] =1
        for i in t:
            if i in d1:
                d1[i]+=1
            else:
                d1[i] =1
        if len(d.keys())!=len(d1.keys()):
            return False

        return d == d1