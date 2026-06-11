class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        numOfIsland = 0

        def bfs(r,c):

            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                surround = [[0,1], [1,0], [0,-1], [-1,0]]

                rq, cq = q.popleft()

                for s in surround:
                    rs, cs = s
                    r, c = rs + rq, cs + cq
                    if (r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == '1'):
                        q.append((r,c))
                        visited.add((r,c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    numOfIsland+=1

        return numOfIsland