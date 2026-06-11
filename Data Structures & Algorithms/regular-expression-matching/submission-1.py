class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(i, j):
            if i in range(len(s)) and j in range(len(p)):
                print(s[i],p[j])
            if i >= len(s) and j >= len(p):
                return True 
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if match:
                if j+1 < len(p) and p[j+1] == '*':
                    if dfs(i+1, j):
                        return True
                    elif dfs(i, j+2):
                        print(i, j+2)
                        return True
                else:
                    if dfs(i+1,j+1):
                        return True
            else:
                if j+1 < len(p) and p[j+1] == '*':
                    if dfs(i, j+2):
                        return True
            return False
        return dfs(0, 0)
                    
