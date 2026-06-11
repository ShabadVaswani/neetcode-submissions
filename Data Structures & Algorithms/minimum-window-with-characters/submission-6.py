class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)< len(t): return ""
        l, r = 0, len(t)
        window, need = {}, {}
        have = 0

        for i in t:
            need[i] = need.get(i,0)+1
            window[i] = 0

        for i in range(len(t)):
            if s[i] in need:
                window[s[i]] = window.get(s[i],0) + 1 
                if window[s[i]] <= need[s[i]]: have += 1

        final = s * 2
        while r < len(s):
            print("w",window)
            print("n",need)
            if have >= len(t):
                if len(final) > len(s[l:r]):
                    final = s[l:r]
                if s[l] in need: 
                    window[s[l]]-=1
                    if window[s[l]] < need[s[l]]:
                        have-=1
                l+=1

            else:
                print("have1", have,len(t))
                if s[r] in need: 
                    
                    print(s[r],window[s[r]] , need[s[r]])
                    if window[s[r]] < need[s[r]]:
                        
                        have+=1
                    window[s[r]]+=1
                    print("have",have)
                r+=1
                    
        while l < len(s):

            if have >= len(t):
                print(have, len(final), r-l)
                if len(final) > r-l:
                    final = s[l:r]
                if s[l] in need: 
                    window[s[l]]-=1
                    if window[s[l]] < need[s[l]]:
                        have-=1
                l+=1
            else: break
        if final == s * 2: return ""
        return final

            



