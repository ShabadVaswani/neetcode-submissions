class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        visited = set()
        res = 0
        dif = 0
        while r < len(s):
            print(l,r, visited)
            if s[r] in visited:
                visited.remove(s[l])
                l+=1

            if s[r] not in visited:
                visited.add(s[r])
                r=r+1
            dif = r-l
            
            
            res = max(res, dif )
        return res
