import math

class Solution:
    def swimInWater(self, grid) -> int:
        print(grid)
        return self.findPath(grid, 0, 0, [])

    def findPath(self, grid, row, col, path):
        print('processing', row, col, grid[row][col])
        path.append(grid[row][col])

        left = right = down = math.inf
        # down path
        if(row < len(grid)-1):
            print('Going down')
            down = self.findPath(grid, row+1, col, path)
            # left path
            if(col > 0):
                print('Going left')
                left = self.findPath(grid, row, col-1, path)
        # right path
        if(col < len(grid[0])-1):
            print('Going right')
            right = self.findPath(grid, row, col+1, path)

        

        minValue = min(max(path), left, right, down)
        print('returninG minvalue ', minValue)
        return minValue

s = Solution()
print(s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))