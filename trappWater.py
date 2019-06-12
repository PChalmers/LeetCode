class solution:
    def trapWater(self, nums):
        if(len(nums) <= 2):
            return 0
        levels = {}
        currentTallest = nums[0]
        total = 0

        for x in range(1,len(nums)):
            if(nums[x] > nums[x-1]):
                # Deal with previous levels if increase
                for x in range(nums[x-1], nums[x]):
                    print('adding key {}'.format(x))
                    self.setLevel(levels, x)
                if(nums[x] >= currentTallest):
                    total += self.dumpLevels(levels)
                    currentTallest = nums[x]
                    print('total is now {}'.format(total))
            elif(nums[x] < nums[x-1]):
                # Deal with new levels if decrease
                for x in range(nums[x-1], nums[x]):
                    print('removing key {} with value {}'.format(x, nums[x]))
                #self.getLevel(levels, x)
            else:
                pass # nums are equal

    def setLevel(self, levels, level):
        if(level in levels):
            levels[level] +=1
        else:
            levels[level] = 1

    def dumpLevels(self, levels):
        returnValue = 0
        for level in levels:
            returnValue += levels[level]
        levels.clear
        return returnValue

s = solution()
print(s.trapWater([0,1,2,1,1,0,3,2,1]))