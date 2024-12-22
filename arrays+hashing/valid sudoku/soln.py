class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if (board[i][j] == "."):
                    continue

                cell_val = int(board[i][j]) - 1 #zero index
                if rows[i][cell_val] or cols[j][cell_val] or boxes[(i // 3) * 3 + (j // 3) ][cell_val]:
                    return False
                
                rows[i][cell_val] = True
                cols[j][cell_val] = True
                boxes[(i // 3) * 3 + (j // 3) ][cell_val] = True

        return True
