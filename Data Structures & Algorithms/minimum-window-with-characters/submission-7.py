class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t => find this, s => from this
        hashone, hashtwo = {}, {}
        have, need = 0, 0
        for i in t:
            hashone[i] = hashone.get(i, 0) + 1
            hashtwo[i] = 0
        need = len(hashone)        
        res = ["", 100000000000]
        l, r = 0, 0
        while  r < len(s):
            if have != need:
                if s[r] in hashtwo:
                    before = hashone[s[r]] <= hashtwo[s[r]]
                    hashtwo[s[r]]+=1
                    after = hashone[s[r]] <= hashtwo[s[r]]
                    if before != after:
                        have+=1
                r+=1
            while have == need:
                print(s[l:r],r-l < res[1])
                if r-l < res[1]:
                    res[0] = s[l:r]
                    res[1] = r-l
                print(res)
                if s[l] in hashtwo:
                    before = hashone[s[l]] <= hashtwo[s[l]]
                    hashtwo[s[l]]-=1
                    after = hashone[s[l]] <= hashtwo[s[l]]
                    if before != after:
                        have-=1
                l+=1
                




        return res[0]

            



