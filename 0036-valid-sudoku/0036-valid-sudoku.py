class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row):
            checklist = []
            for i in range(9):
                if (row[i] != "." and row[i] in checklist):
                    return False
                checklist.append(row[i])
            return True
        def checkCol(board, col):
            checklist = []
            for i in range(9):
                if board[i][col] != "." and board[i][col] in checklist:
                    return False
                checklist.append(board[i][col])
            return True
		
        # row checking
        for i in range(9):
            if (checkRow(board[i]) == False):
                return False
                
        # column checking
        for j in range(9):
            if (checkCol(board, j) == False):
                return False
                
        # box checking
        for k in range(0,9,3):
            for m in range(0,9,3):
                if (checkRow(board[k][m:m+3] + board[k+1][m:m+3] + board[k+2][m:m+3]) == False):
                    return False
                    
        return True
        