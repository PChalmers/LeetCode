from math import sqrt

class Solution:
    def isValidSudoku(self, board) -> bool:
        boardSize = len(board)
        # process rows
        for row in board:
            self.check = checkValues(boardSize)
            for index in range(boardSize):
                if(not self.check.checkValue( row[index] )):
                    return 'false'

        # process columns
        for index in range(boardSize):
            self.check = checkValues(boardSize)
            for row in board:
                if(not self.check.checkValue( row[index] )):
                    return 'false'

        # process cells
        cellDim = int(sqrt(boardSize))
        for vStartInd in [x*cellDim for x in range(cellDim)]:
            for hStartInd in [x*cellDim for x in range(cellDim)]:
                self.check = checkValues(boardSize)
                for hIndex in range(hStartInd,hStartInd + cellDim):
                    for vIndex in range(vStartInd,vStartInd + cellDim):
                        if(not self.check.checkValue( board[hIndex][vIndex] )):
                            print(hIndex, vIndex, board[hIndex][vIndex])
                            return 'false'

        return 'true'

class checkValues:
    def __init__(self, maxValue):
        self.maxValue = maxValue
        self.checkedValues = []
    def checkValue(self, value: str) ->bool:
        if(value == '.'):
            return True
        try:
            val = int(value)
        except ValueError:
            return False
        if(val in self.checkedValues):
            return False
        self.checkedValues.append(val)
        return True





s = Solution()

sud = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(s.isValidSudoku(sud))

sud = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(s.isValidSudoku(sud))
