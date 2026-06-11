class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = s.split(" ")
        st = "".join(ls)
        stl = st.lower()
        ls = list(stl)
        lastpt = len(ls)-1
        for i in ls:
            if i.isalnum() == False:
                if ls[lastpt].isalnum() == False:
                    lastpt-=1
                continue
            if ls[lastpt].isalnum() == False:
                lastpt-=1
                
            
            if i !=ls[lastpt]:
                return False
            lastpt -= 1
        return True
        