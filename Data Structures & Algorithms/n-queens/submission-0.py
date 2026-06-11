class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negDiag = set() # r-c
        posDiag = set() # r+c

        res = []

        board = [ ['.'] * n for i in range(n)]

        def bkt(r):

            if r == n:
                copy = [''.join(x) for x in board]
                res.append(copy)
                return

            for c in range(len(board[r])):
                if c in cols or (r-c) in negDiag or (r+c) in posDiag:
                    continue

                cols.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)
                board[r][c] = 'Q'

                bkt(r+1)

                cols.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                board[r][c] = '.'


        bkt(0)

        return res









