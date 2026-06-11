class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxSizeOfIsland = 0

        def bfs(r,c):

            q = deque()
            q.append((r,c))
            visited.add((r,c))
            size = 1

            while q:
                surround = [[0,1], [1,0], [0,-1], [-1,0]]

                rq, cq = q.popleft()

                for s in surround:
                    rs, cs = s
                    r, c = rs + rq, cs + cq
                    if (r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1):
                        q.append((r,c))
                        visited.add((r,c))
                        size += 1
            return size



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    size = bfs(r,c)
                    print(size)
                    if size > maxSizeOfIsland:
                        maxSizeOfIsland = size

        return maxSizeOfIsland