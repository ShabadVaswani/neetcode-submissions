class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        visited = set()
        res = 0
        dif = 0
        while r < len(s):
            print(l,r, visited)
            while s[r] in visited:
                visited.remove(s[l])
                l+=1

            visited.add(s[r])
            r=r+1
            dif = r-l
            
            res = max(res, dif )
        return res
