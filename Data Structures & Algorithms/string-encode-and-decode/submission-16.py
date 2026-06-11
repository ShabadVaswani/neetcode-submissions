class Solution:

    def encode(self, strs: List[str]) -> str:
        lstofstringparts = []
        for s in strs:
            length = len(s)
            lstofstringparts.extend( [str(length) ,'#' , s]) 
        print("".join(lstofstringparts))
        return  "".join(lstofstringparts)
    def decode(self, s: str) -> List[str]:        
        print(s)
        num = ''
        st = ''
        x = False
        lst = []
        while len(s) > 0:
            hashpt = s.find('#')
            le = int(s[0:hashpt])
            s = s[hashpt+1:]
            lst.append(s[0:le])
            s = s[le:]

            
            

        return lst
