class Solution:
    def largestRectangleArea(self, heights):
        # Check for invalid input
        if(heights == None or len(heights) == 0):
            return 0

        # Solve largest rect under histogram
        stackOfPastIndexes = []
        maxRectSize = 0
        histLen = len(heights)
        for currentHeightIndex in range(histLen+1):
            # Add 1 more loop to deal with the last num in the array
            cur = -1 if (currentHeightIndex == histLen) else heights[currentHeightIndex]
            # If the current col is lower than the previous Iterate through the previous 
            # columns that are higher
            while (len(stackOfPastIndexes) != 0 and cur < heights[stackOfPastIndexes[-1]]):
                heightWeAreChecking = heights[stackOfPastIndexes.pop(-1)]
                numRowsStacked = currentHeightIndex if len(stackOfPastIndexes) == 0 else  currentHeightIndex - stackOfPastIndexes[-1] - 1
                maxRectSize = max(heightWeAreChecking * numRowsStacked, maxRectSize)
            stackOfPastIndexes.append(currentHeightIndex)
        
        return maxRectSize

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3])) # 10
print(s.largestRectangleArea([3, 1, 3, 2, 2]))