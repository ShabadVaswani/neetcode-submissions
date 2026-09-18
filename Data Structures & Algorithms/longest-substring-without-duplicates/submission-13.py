class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}
        mx = 0
        k = 0
        minposrep = 0

        for i in range(len(s)):
            if s[i] in st:
                mx=max(k,mx)
                k = i - max(minposrep,st[s[i]]) #-> location of c
                #print(k,i, max(minposrep,st[s[i]]), minposrep, s[i])
                minposrep = max(minposrep,st[s[i]])
                #print('minposrep',minposrep)
                st[s[i]] = i

            else:
                k+=1
                #print(k,i)
                st[s[i]] = i
            #print(k,mx)
        return max(k,mx)

            