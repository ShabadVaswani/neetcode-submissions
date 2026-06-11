class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return "empty"
        return "pl;;s".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        return s.split('pl;;s')
