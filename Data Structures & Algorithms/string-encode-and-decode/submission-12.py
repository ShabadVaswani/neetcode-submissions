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
        if s == '0#':
            return [""]
        print(s)
        num = ''
        st = ''
        x = False
        lst = []
        for i in list(s):
            if i !='#' and x == False:
                print(num, i)
                num = num + i
                print(num)
            if x and num > 0:
                num -= 1
                st = st + i
            if i == '#' and x == False:
                x = True
                num = int(num)
            if num == 0:
                num = ''
                x = False
                lst.append(st)
                st = ''
            

        return lst
