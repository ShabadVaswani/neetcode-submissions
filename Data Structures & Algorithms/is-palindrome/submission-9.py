class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        l = len(s)-1
        x = len(s)
        i = 0
        pk = 0
        while i < l:
            
            
            while i < l and self.alphanum(s[i])!=True :
                i+=1
            while i < l and self.alphanum(s[l])!=True:
                l-=1
            if s[i].lower() != s[l].lower():
                print(s[i],l)
                return False
            i+=1
            l-=1
        return True
    def alphanum(self, c):
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9'):
            return True
        return False
