class Solution:

    def encode(self, strs: List[str]) -> str:
        string = "--no--input"
        for s in strs:
            if string == "--no--input":
                string = ""
            length = len(s)
            string = string + str(length) + '#' + s 
        print(string)
        return  string
    def decode(self, s: str) -> List[str]:
        if s == '--no--input':
            return []
        
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
