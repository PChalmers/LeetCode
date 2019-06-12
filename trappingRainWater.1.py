class Solution:
    def trap(self, height) -> int:
        if(len(height) <= 2):
            return 0
        previousHighest = [-1,-1]
        total = startPoint = 0

        # find first Highest part - first decrease in height
        for index in range(len(height)):
            if(height[index] < previousHighest[1]):
                startPoint = index # Previous index is new hieghest
                break
            else:
                previousHighest = [index,height[index]]

        # found first highest part so now process middle part where water can collect
        for index in range(startPoint, len(height)):
            # Do nothing until finding a larger height or the end of the list
            if(height[index] <= previousHighest[1]):
                pass
            else: # Found new highest so process up to this point
                total += self.processIntermediateHeights(height, index, previousHighest)
                previousHighest = [index, height[index]]
        
        # Check that there are unprocessed height after the higest part
        if(previousHighest[0] != len(height)-1): # and height[-1] > 0):
            total += self.processLastHeights(height, previousHighest)

        return total

    def processIntermediateHeights(self, height, currentH, prevH):
        total = 0
        for index in range(currentH, prevH[0], -1):
            diff = prevH[1] - height[index]
            total += diff if diff > 0 else 0
        return total

    def processLastHeights(self, height, prevH):
        addToTotal = 0
        currentHighest = height[-1] # First height to compare is the last in the list

        # Iterate backwards from the end point to the previous max height
        for index in range(len(height)-1, prevH[0], -1):
            indexedHeight = height[index]
            if(indexedHeight < currentHighest):
                diff = currentHighest - indexedHeight
                addToTotal += diff 
            else:
                currentHighest = indexedHeight
        return addToTotal

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,0,1,1,2,1])) # 9
print(s.trap([4,2,3])) # 1
print(s.trap([2,6,3,8,2,7,2,5,0])) # 11