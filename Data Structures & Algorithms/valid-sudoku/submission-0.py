class Solution:
    def isValidSection(self, line: List[str]) -> bool:
        temp_line = [x for x in line if x != '.']
        for j in range(len(temp_line)):
            if temp_line.count(temp_line[j]) != 1:
                return False
        return True
    
    def getSquares(self, board: List[List[str]]) -> List[List[str]]:
        squares = [[] for _ in range(9)]
        start_row = 0
        square_index = 0
        for i in range(3):
            start_col = 0
            for j in range(3):
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        squares[square_index].append(board[row][col])

                start_col += 3
                square_index += 1

            start_row += 3

        return squares
                

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if not self.isValidSection(board[i]) or not self.isValidSection(column):
                return False
        squares = self.getSquares(board)
        for square in squares:
            if not self.isValidSection(square):
                return False
        return True