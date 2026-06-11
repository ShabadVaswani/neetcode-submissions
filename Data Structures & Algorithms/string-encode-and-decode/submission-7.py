class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return '*[*[*'
        if len(strs) == 1: return strs[0]
        enc = ''
        for x in range(len(strs)-1):
            enc = enc + strs[x]
            enc = enc + '*[*[*'
        enc = enc + strs[-1]
        return enc
        


    def decode(self, s: str) -> List[str]:
        if s == '*[*[*': return []
        return s.split('*[*[*')
