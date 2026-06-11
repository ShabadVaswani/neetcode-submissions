class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        paci_reach = [[False for _ in range(cols)] for _ in range(rows)]
        atla_reach = [[False for _ in range(cols)] for _ in range(rows)]

        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        def dfs(r, c, reachable):
            reachable[r][c] = True
            for dr, dc in directions:
                nr, nc = r+dr,c+dc

                if nr in range(rows) and nc in range(cols) and heights[nr][nc] >= heights[r][c] and not reachable[nr][nc]:
                    dfs(nr,nc, reachable)

        for c in range(cols):
            dfs(0,c,paci_reach)
            dfs(rows-1,c,atla_reach)

        for r in range(rows):
            dfs(r,0,paci_reach)
            dfs(r,cols-1,atla_reach)

        result = []

        for r in range(rows):
            for c in range(cols):
                if paci_reach[r][c] and atla_reach[r][c]:
                    result.append([r,c])

        return result