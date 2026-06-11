class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        infi = 2147483647
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))

        dist = 0
        nxt = [(0,-1), (0, 1), (1, 0), (-1, 0)]
        while q:
            for _ in range(len(q)):
                (i, j) = q.popleft()
                for (k, l) in nxt:
                    if i + k in range(len(grid)) and j + l in range(len(grid[0])) and grid[i+k][j+l] == 1:
                        grid[i+k][j+l] = 2
                        q.append((i+k, j+l))
            if len(q) == 0:
                break
            dist+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return dist