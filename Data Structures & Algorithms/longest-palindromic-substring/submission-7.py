class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(0, len(s)):
            k=1
            while True:
                if i-k in range(len(s)) and i+k in range(len(s)):
                    if s[i-k] != s[i+k]:
                        break
                    else:
                        
                        if len(res) < 2*k+1:
                            res = s[i-k:i+k+1]
                else:
                    break
                k+=1
            k=0
            while True:
                if i-k in range(len(s)) and i+k+1 in range(len(s)):
                    if s[i-k] != s[i+k+1]:
                        break
                    else:
                        print(i, s[i-k],s[i+k+1])
                        
                        if len(res) < 2*(k+1):
                            res = s[i-k:i+k+2]
                else:
                    break
                k+=1
            

        return res
