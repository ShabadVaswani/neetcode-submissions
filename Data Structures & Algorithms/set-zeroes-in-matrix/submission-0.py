class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeror = set()
        zeroc = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeror.add(i)
                    zeroc.add(j)

        for r in zeror:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
        for c in zeroc:
            for i in range(len(matrix )):
                matrix[i][c] = 0