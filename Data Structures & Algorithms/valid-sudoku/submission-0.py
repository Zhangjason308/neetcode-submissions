class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Input is a list of lists, where each list reps the row
        # Empty number is represented by "."
        # Conditions to be met
        # 1. Each row must have unique values
        # 2. Each column must have unique values
        # 3. Each third must have unique values

        square_set = {}
        for x in range(len(board)):
            column_set = set()
            for y in range(len(board)):
                if board[x][y] == ".":
                    continue
                elif board[x][y] not in column_set:
                    column_set.add(board[x][y])
                else:
                    return False
        
        for x in range(len(board)):
            row_set = set()
            for y in range(len(board)):
                if board[y][x] == ".":
                    continue
                elif board[y][x] not in row_set:
                    row_set.add(board[y][x])
                else:
                    return False

        for square in range(len(board)):
            square_set = set()

            for x in range(len(board) // 3):
                for y in range(len(board) // 3):
                    r = (square // 3) * 3 + x
                    c = (square % 3) * 3 + y
                    if board[r][c] == ".":
                        continue
                    elif board[r][c] not in square_set:
                        square_set.add(board[r][c])
                    else:
                        return False
        return True