class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hashmap = {}
        res = 0
        maxval = 0
        window = r-l+1
        while r < len(s):
            print(r, l, hashmap)
            # print(res, maxval, window)
            if s[r] in hashmap:
                hashmap[s[r]]+=1
            else:
                hashmap[s[r]] = 1
            maxval = max(hashmap[s[r]], maxval)
            

            window = r-l+1
            
            while window - maxval > k and l < r :
                print(window-maxval, l, r)
                hashmap[s[l]]-=1
                l+=1
                window = r-l+1
            
            
            res = max(window, res)
            r+=1
        return res