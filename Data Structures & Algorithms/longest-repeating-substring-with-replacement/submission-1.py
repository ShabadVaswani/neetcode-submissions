class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            replaceables = r-l - max(count.values())+1
            print(replaceables, res)
            if replaceables > k:
                count[s[l]] = count.get(s[l])-1
                l+=1
            else:
                res = max(res, r-l+1)
                r+=1
                if(res==5):print('l: ', l, 'r: ',r, replaceables)
            print(res, '\n')

        return res
