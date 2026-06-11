class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        la = deque()
        sa = set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    la.append((i,j))
                    sa.add((i,j))
        adj = [(0,1), (0,-1), (-1,0), (1,0)]
        while la:
            (i,j) = la.popleft()
            for k,l in adj:
                if i+k in range(len(heights)) and j + l in range(len(heights[0])) and (i+k, j+l) not in sa and heights[i+k][j+l] >= heights[i][j]:
                    la.append((i+k, j+l))
                    sa.add((i+k,j+l))
        lp = deque()
        sp = set()
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == len(heights)-1 or j == len(heights[0])-1:
                    lp.append((i,j))
                    sp.add((i,j))
                    
        adj = [(0,1), (0,-1), (-1,0), (1,0)]
        while lp:
            (i,j) = lp.popleft()
            for k,l in adj:
                if i+k in range(len(heights)) and j + l in range(len(heights[0])) and (i+k, j+l) not in sp and heights[i+k][j+l] >= heights[i][j]:
                    lp.append((i+k, j+l))
                    sp.add((i+k,j+l))
        for i in sa:
            if i in sp:
                res.append(i)
        return res
            

        
            
