class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        row_set = defaultdict(list)
        col_set = defaultdict(list)
        subboxes_set = defaultdict(list)

        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val != ".":
                    if val in row_set[r]:
                        return False
                    elif val not in row_set[r]:
                        row_set[r].append(val)
                    
                    if val in col_set[c]:
                        return False
                    elif val not in col_set[c]:
                        col_set[c].append(val)

                    if val in subboxes_set[(r // 3, c // 3)]:
                        return False
                    elif val not in subboxes_set[(r // 3, c // 3)]:
                        subboxes_set[(r // 3, c // 3)].append(val)

        return True