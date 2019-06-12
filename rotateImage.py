class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if(len(matrix) <= 0):
            return

        for ring in range(len(matrix)//2):
            for index in range(len(matrix)-1 - ring*2):
                numCols = len(matrix[0])-1
                numRows = len(matrix)-1

                # topleft = matrix[ring][ring + index]
                # topright = matrix[ring + index][numCols - ring]
                # bottomleft = matrix[numRows - ring - index][ring]
                # bottomRight = matrix[numRows - ring][numCols - ring - index]     
                # temp = topleft
                # topleft = bottomleft
                # bottomleft = bottomRight
                # bottomRight = topright
                # topright = temp
                temp = matrix[ring][ring + index]
                matrix[ring][ring + index] = matrix[numRows - ring - index][ring]
                matrix[numRows - ring - index][ring] = matrix[numRows - ring][numCols - ring - index]  
                matrix[numRows - ring][numCols - ring - index]   = matrix[ring + index][numCols - ring]
                matrix[ring + index][numCols - ring] = temp


matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:
    print(row)
s = Solution()
s.rotate(matrix)
for row in matrix:
    print(row)

matrix2 = [  [ 5, 1, 9,11],  [ 2, 4, 8,10],  [13, 3, 6, 7],  [15,14,12,16]]
for row in matrix2:
    print(row)
s.rotate(matrix2)
for row in matrix2:
    print(row)