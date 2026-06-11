class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r-l):
                top, bottom = l,r
                topleft = matrix[top][l+i]
                topright = matrix[top+i][r]
                bottomleft = matrix[bottom-i][l]
                bottomright = matrix[bottom][r-i]
                matrix[top][l+i], matrix[bottom-i][l], matrix[bottom][r-i], matrix[top+i][r]  = bottomleft, bottomright, topright, topleft
            l+=1
            r-=1
        return 
