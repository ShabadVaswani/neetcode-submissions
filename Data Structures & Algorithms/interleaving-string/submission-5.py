class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 1 and len(s2) == 0 or  len(s2) == 1 and len(s1) == 0:
            if s3 == max(s1, s2):
                return True
            return False

        grid = [[0 for j in range(len(s1)+1)] for i in range(len(s2)+1)]
        if len(grid) == 0:
            return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if i == 0 and j == 0:
                    grid[0][0] = True
                    continue
                elif i == 0:
                    if j <= len(s1) and s3[j-1] == s1[j-1] and grid[0][j-1] == True:
                        grid[0][j] = True
                        continue
                    else:
                        grid[0][j] = False
                elif j == 0:
                    if  i <= len(s2) and s3[i-1] == s2[i-1] and grid[i-1][0] == True:
                        grid[i][0] = True
                        continue
                    else:
                        grid[i][0] = False
                if s3[i+j-1] == s1[j-1] :
                    if  grid[i][j-1] == True:
                        grid[i][j] = True
                        continue
                    
                if  s3[i+j-1] == s2[i-1]:
                    if grid[i-1][j] == True:
                        grid[i][j] = True
                        continue
                    else: 
                        grid[i][j] = False
                else: 
                    grid[i][j] = False

                    


    
        return grid[-1][-1]

            