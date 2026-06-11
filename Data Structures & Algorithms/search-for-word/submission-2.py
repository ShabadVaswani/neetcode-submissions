class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag = False

        def dfs(i, j, k):
            if k == len(word):
                return True
            print(word[k], board[i][j])
            temp = board[i][j]
            board[i][j] = '#'
            flag = False
            
            if i+1 in range(0, len(board)) and board[i+1][j] == word[k]:
                flag = flag or dfs(i+1, j, k+1)
            if i-1 in range(0, len(board)) and board[i-1][j] == word[k]:
                flag = flag or dfs(i-1, j, k+1)
            if j+1 in range(0, len(board[0])) and board[i][j+1] == word[k]:
                flag = flag or dfs(i, j+1, k+1)
            if j-1 in range(0, len(board[0])) and board[i][j-1] == word[k]:
                flag = flag or dfs(i, j-1, k+1)

            board[i][j] = temp
            return flag

                
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    sol = dfs(i, j, 1)
                    flag = flag or sol

        return flag

        

