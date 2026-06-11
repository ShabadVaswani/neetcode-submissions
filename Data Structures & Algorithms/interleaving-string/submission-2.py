class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}

        def dfs(n,m):
            if (n,m) in dp:
                return dp[(n,m)]
            if n+m >= len(s3):
                dp[(n,m)] = True
                return True
            if n >= len(s1) and m >= len(s2):
                dp[(n,m)] = False
                return False
                
            if (n < len(s1) and s1[n] == s3[n+m]): 
                if dfs(n+1, m) :
                    dp[(n,m)] = True
                    return True
                    return True
            if (m < len(s2) and s2[m] == s3[n+m]):
                if  dfs(n, m+1):
                    dp[(n,m)] = True
                    return True
            dp[(n,m)] = False
            return False

        return dfs(0,0)

            