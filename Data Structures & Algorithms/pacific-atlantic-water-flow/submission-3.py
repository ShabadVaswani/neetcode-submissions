class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.la = deque()
        self.sa = set()
        self.lp = deque()
        self.sp = set()
        res = []

        def dfsa(i,j):
            adj = [(0,1), (0,-1), (-1,0), (1,0)]
            for k,l in adj:
                if i+k in range(len(heights)) and j + l in range(len(heights[0])) and \
                (i+k, j+l) not in self.sa and heights[i+k][j+l] >= heights[i][j]:
                    self.la.append((i+k, j+l))
                    self.sa.add((i+k,j+l))
                    dfsa(i+k,j+l)
        def dfsp(i,j):
            adj = [(0,1), (0,-1), (-1,0), (1,0)]
            for k,l in adj:
                if i+k in range(len(heights)) and j + l in range(len(heights[0])) and \
                (i+k, j+l) not in self.sp and heights[i+k][j+l] >= heights[i][j]:
                    self.lp.append((i+k, j+l))
                    self.sp.add((i+k,j+l))
                    dfsp(i+k,j+l)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    self.la.append((i,j))
                    self.sa.add((i,j))
                    dfsa(i,j)
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == len(heights)-1 or j == len(heights[0])-1:
                    self.lp.append((i,j))
                    self.sp.add((i,j))
                    dfsp(i,j)
                    
        for i in self.sa:
            if i in self.sp:
                res.append(i)
        return res
            

        
            
