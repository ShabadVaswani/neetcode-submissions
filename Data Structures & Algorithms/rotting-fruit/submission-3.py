class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        q = deque()

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

                fresh = addToQ(r-1,c, fresh)
                fresh = addToQ(r,c-1, fresh)
                fresh = addToQ(r+1,c, fresh)
                fresh = addToQ(r,c+1, fresh)
            time+=1
        if fresh:
            return -1 
        return time
