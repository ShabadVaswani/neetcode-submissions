class Solution:
    def palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1

        return True

    def partition(self, s: str) -> List[List[str]]:

        res = []
        path = []
        
        def dfs(startindex):
            if startindex >= len(s):
                res.append(path[:])
                return
            for i in range(startindex, len(s)):
                if self.palindrome(s, startindex, i):
                    path.append(s[startindex:i+1])
                    dfs(i+1)
                    path.pop()

            return
        dfs(0)
        print(res)
        return res


            




