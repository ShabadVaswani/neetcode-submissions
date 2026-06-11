class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        def conquer(i,j):
            if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] == 0 or grid[i][j] == 2:
                return 0
            print(i,j)
            grid[i][j] = 2
            area = conquer(i+1, j)
            area+=conquer(i-1,j)
            area+=conquer(i,j-1)
            area+=conquer(i,j+1)
            return area +1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res, conquer(i,j))
        
        return res