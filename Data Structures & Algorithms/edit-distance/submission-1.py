class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        matrix = [[0 for w in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for i in range(len(matrix)):#compare with empty
            matrix[i][-1] = len(matrix)-i-1
        for j in range(len(matrix[0])):
            matrix[-1][j] = len(matrix[0]) - j - 1
        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word1)-1, -1, -1):
                if word1[j] == word2[i]:
                    matrix[i][j]=matrix[i+1][j+1]
                else:
                    matrix[i][j] = 1+min(matrix[i+1][j+1], matrix[i+1][j], matrix[i][j+1])
        print(matrix)
        return matrix[0][0]

                