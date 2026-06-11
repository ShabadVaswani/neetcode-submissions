class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2: return False
        d1 = [0]*26
        d2 = [0]*26
        for i in range(len(s1)):
            d1[ord(s1[i])-ord('a')] += 1
            d2[ord(s2[i])-ord('a')] += 1

        for i in range(len(s2)):
            print(d1, d2)
            if d1 == d2: 
                return True
            d2[ord(s2[i])-ord('a')]-=1
            print(ord(s2[i])-ord('a'))
            if i < len(s2)-len(s1): 
                d2[ord(s2[i+len(s1)])-ord('a')] += 1

        return False
