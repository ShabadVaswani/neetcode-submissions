class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispali(i, j):
            print('f',s[i:j],'gas', s[i], s[j])
            while i < j:
                if s[i] !=s[j]:
                    return False
                i+=1
                j-=1
            return True


        res = []
        path = []            
        def dfs(i):

            if i >= len(s):
                res.append(path[:])
                return

            for j in range(i, len(s)):
                if ispali(i, j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop(-1)

        dfs(0)
        return res