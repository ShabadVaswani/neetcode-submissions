class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hashmap = {}
        res = 0
        maxval = 0
        while r < len(s):
            print(r, l, hashmap)
            # print(res, maxval, window)
            if s[r] in hashmap:
                hashmap[s[r]]+=1
            else:
                hashmap[s[r]] = 1
            maxval = max(hashmap[s[r]], maxval)
            

            
            while r-l+1 - maxval > k and l < r :
                hashmap[s[l]]-=1
                l+=1
            
            
            res = max(r-l+1, res)
            r+=1
        return res