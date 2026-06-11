class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visited = set()
        islands = 0

        def dfs(r,c):
            q = collections.deque()

            q.append((r,c))
            visited.add((r,c))

            while q:
                surround = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                rq,cq = q.popleft()
                for rs, cs in surround:
                    ru, cu = rq + rs, cq + cs
                    if(ru in range(rows) and cu in range(cols) and (ru,cu) not in visited and grid[ru][cu] == '1'):
                        visited.add((ru,cu))
                        q.append((ru,cu))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    islands+=1
        return islands