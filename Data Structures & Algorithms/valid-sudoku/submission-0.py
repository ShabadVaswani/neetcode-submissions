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
                if current in rows[i]:
                    return False
                else:
                    rows[i].add(current);
                if current in cols[j]:
                    print(current)
                    return False
                else:
                    cols[j].add(current);
                if current in boxs[str([i//3,j//3])]:
                    print(boxs[str([i//3,j//3])])
                    print(current, i//3, j//3)
                    return False
                else:
                    boxs[str([i//3,j//3])].add(current);
        print(cols, rows, boxs)
        return True

                
