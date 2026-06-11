class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s1 = [*s]
        s1.sort()
        t1 = [*t]
        t1.sort()
        print(s)

        if len(t1) != len(s1):
            return False

        for i in range(len(s1)):
            if s1[i] != t1[i]:
                return False
        return True
