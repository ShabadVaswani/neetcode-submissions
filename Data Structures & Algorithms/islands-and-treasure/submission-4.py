class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        infi = 2147483647
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))

        dist = 1
        nxt = [(0,-1), (0, 1), (1, 0), (-1, 0)]
        while q:
            for _ in range(len(q)):
                (i, j) = q.popleft()
                for (k, l) in nxt:
                    if i + k in range(len(grid)) and j + l in range(len(grid[0])) and grid[i+k][j+l] > dist:
                        grid[i+k][j+l] = dist
                        q.append((i+k, j+l))
            dist+=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print(grid[i][j])

            
