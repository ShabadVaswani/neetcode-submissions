class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        q = deque()
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        fresh, time = 0, 0
        def addToQ(r, c, fresh):
            if r in range(row) and c in range(col) and grid[r][c] == 1:
                grid[r][c] = 2
                fresh -=1
                q.append([r,c])
            return fresh

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append([r,c])

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr in range(row) and nc in range(col) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -=1
                        q.append([nr,nc])
            time+=1
        if fresh:
            return -1 
        return time
