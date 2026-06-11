class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = list(s)
        i = 0
        while i < len(ls):
            if ls[i].isalnum() == False:
                ls.remove(ls[i])
                i-=1
            i+=1
        st="".join(ls)
        stl = st.lower()
            #print(stl[i])
        for i in range(len(stl)):
            print(stl)
            #print(stl[i],stl[-i-1])
            if stl[i] != stl[-i-1]:
                
                print(stl[i],stl[-i-1])
                return False
        return True


        