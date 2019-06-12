class Solution:
    def maximalRectangle(self, matrix):
        # Check for invalid input
        if (matrix == None or len(matrix) == 0):
            return 0
        numRows = len(matrix)
        numCols = len(matrix[0])
        # Check for size 0 matrix
        if(numRows*numCols == 0):
            return 0
        maxRectSize = 0

        colHeights = [0]*numCols
        for row in range(numRows):
            # Create histogram of columns top down for current row
            for col in range(numCols):
                if (matrix[row][col] == '1'):
                    colHeights[col] += 1
                else:
                    colHeights[col] = 0
            # Solve largest rect under histogram
            print(row, colHeights)
            stack = []
            for currentHeight in range(numCols+1):
                # Add 1 more loop to deal with the last num in the array
                cur = -1 if (currentHeight == numCols) else colHeights[currentHeight]
                # If the current col is lower than the previous Iterate through the previous 
                # columns that are higher
                while (len(stack) != 0 and cur < colHeights[stack[-1]]):
                    heightWeAreChecking = colHeights[stack.pop(-1)]
                    numRowsStacked = currentHeight if len(stack) == 0 else  currentHeight - stack[-1] - 1
                    maxRectSize = max(heightWeAreChecking * numRowsStacked, maxRectSize)
                stack.append(currentHeight)
        
        return maxRectSize

s = Solution()
print(s.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))
print(s.maximalRectangle([[],[]]))

