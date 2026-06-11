class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        q = deque()
        rotten = set()
        minutes = -1
        totalHealthy = 0
        totalUnhealthy = 0

        def addToQ(r,c):
            if r in range(row) and c in range(col) and (r,c) not in rotten and grid[r][c] == 1:
                q.append([r,c])
                rotten.add((r,c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append([r,c])
                    rotten.add((r,c))
                    totalUnhealthy +=1
                if grid[r][c] == 1:
                    totalHealthy +=1
        print(q)
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] == 1:
                    totalHealthy -=1
                    totalUnhealthy +=1
                grid[r][c] = 2
                
                

                addToQ(r-1,c)
                addToQ(r,c-1)
                addToQ(r+1,c)
                addToQ(r,c+1)
            
            minutes+=1
        if totalHealthy:
            return -1
                    
        if not totalUnhealthy:
            return 0
        return minutes