class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r,c):
            if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]!=-1:
                q.append([r,c])
                visit.add((r,c))
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append([r,c])
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r,c-1)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r+1,c)

            dist+=1


        