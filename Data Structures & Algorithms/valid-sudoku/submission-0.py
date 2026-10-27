class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        boxes = [[ set() for _ in range(3) ] for _ in range(3) ]

        for i in range(len(board)):
            for j in range(len(board[1])):
                item = board[i][j]
                if item == ".":
                    continue
                    
                sets = rows[i], cols[j], boxes[i // 3][j // 3]
                for s in sets:
                    if item in s:
                        return False
                    s.add(item)
        return True
        