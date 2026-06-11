class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        row = [0] * (len(text1)+1)

        for i in range(len(text2)-1, -1, -1):
            newRow = [0] * (len(text1)+1)
            for j in range(len(text1)-1, -1, -1):
                if text1[j] == text2[i]:
                    newRow[j] = 1 + row[j+1]
                else:
                    newRow[j] = max(row[j] , newRow[j+1])
            row = newRow

            



        return row[0]