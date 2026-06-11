class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i, j):
            print(i, j)
            if i not in range(0, len(grid)) or j not in range(0, len(grid[0])) or grid[i][j] == 0:
                return 1
            else:
                if (i,j) in visited:
                    return 0
                visited.add((i,j))
                p = dfs(i+1,j)
                p += dfs(i-1,j)
                p += dfs(i,j+1)
                p += dfs(i,j-1)
                return p
            
            
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)
            
            
                

                         
