from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        def validate(i,j, x):
            for k in range(len(board)):
                if  board[k][j] == x:
                    return False
            for k in range(len(board[0])):
                if  board[i][k] == x:
                    return False
            for k in [3*(i//3), 3*(i//3)+1, 3*(i//3)+2]:
                for l in  [3*(j//3), 3*(j//3)+1, 3*(j//3)+2]:
                    if board[k][l] == x:
                        return False
            return True

        def bt(i,j):
            print("enter", i,j, n)
            print(board)
         
            while i < n and board[i][j] != ".":
                print (i,j, board[i][j])
                i, j = i + (j+1)//n, (j+1)%n
            if i == n : return True              
            for x in "123456789":
                if validate(i,j,x):
                    board[i][j]=x
                    if bt(i,j): return True
                    board[i][j]="."
            print("exit", i,j, n)
            return False
        bt(0,-1)  
                    
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# board = [["5","3","."], ["6",".","."],[".", "9","8"]]
print(Solution().solveSudoku(board))
print(board)