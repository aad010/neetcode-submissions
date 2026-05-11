class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            given 9 x 9 sudoku board 
                valid if row contains digits 1-9 no dups
                      if column contains digits 1-9 no dups
                      each of nine subboxes contain 1-9 no dups

        '''
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                
                if (board[row][col] in columns[col] or board[row][col] in rows[row] or board[row][col] in squares[(row // 3, col // 3)]):
                    return False
                
                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        
        return True
        