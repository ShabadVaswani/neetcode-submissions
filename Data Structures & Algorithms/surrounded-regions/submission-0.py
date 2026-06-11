class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0] ]
        def captureDFS(r,c):
            if r in range(rows) and c in range(cols) and board[r][c] == 'O':
                board[r][c] ='T'
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    captureDFS(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows-1] or c in [0, cols-1]):
                    captureDFS(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'



            


                