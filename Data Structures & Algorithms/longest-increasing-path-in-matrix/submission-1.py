class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        lip = {} 
        res = 0
        def dfs(i,j):
            if (i,j) in lip:
                return lip[(i,j)]
            curr = matrix[i][j]
            surround = [(0,1), (1,0), (0,-1), (-1,0)]
            tempres = 0
            for (l,m) in surround:
                if i+l in range(len(matrix)) and j+m in range(len(matrix[0])):
                    surr = matrix[i+l][j+m]
                    if curr < surr:
                        tempres = max(tempres,dfs(i+l, j+m))
            lip[(i,j)] = 1+tempres
            return 1+tempres
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = matrix[i][j]
                res = max(res,dfs(i,j))

        return res
                