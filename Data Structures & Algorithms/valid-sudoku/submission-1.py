class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set);
        rows = collections.defaultdict(set);
        boxs = collections.defaultdict(set);
        for i in range(9):
            for j in range(9):
                current = board[i][j] 
                if current == ".":
                    continue
                if current in rows[i] or current in cols[j] or current in boxs[(i//3,j//3)]:
                    return False
                rows[i].add(current);
                cols[j].add(current);
                boxs[(i//3,j//3)].add(current);
        print(cols, rows, boxs)
        return True

                
