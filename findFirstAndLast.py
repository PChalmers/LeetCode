class Solution:
    # Sorted so values are in a row in the array
    def searchRange(self, nums, target):
        findMin = findMax = self.findValue(nums, target, 0, len(nums)-1)
        if(findMin == -1): return -1,-1
        while(True): 
            if(findMin-1 >= 0 and nums[findMin-1] == target):
                findMin -=1
            else:
                break
        while(True): 
            if(findMax+1 < len(nums) and nums[findMax+1] == target):
                findMax +=1
            else:
                break
        return findMin, findMax

    # Find the value in the list, not confirmed how many 
    def findValue(self, nums, target, rangeStart, rangeEnd):
        if(rangeStart > rangeEnd):
            return -1
        midPoint = (rangeEnd + rangeStart) // 2
        if(nums[midPoint] == target):
            return midPoint
        if(nums[midPoint] > target):
            return self.findValue(nums, target, rangeStart, midPoint-1)
        else:
            return self.findValue(nums, target, midPoint+1, rangeEnd)

s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))
print(s.searchRange([5,7,7,8,8,10],6))
print(s.searchRange([5,7,7,8,8,10],5))
print(s.searchRange([5,7,7,8,8,10],10))
print(s.searchRange([1,1,2],1))

