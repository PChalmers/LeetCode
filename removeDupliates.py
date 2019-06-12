class Solution:
    def removeDuplicates(self, nums):
        if(len(nums) == 0):
            return 0
        previous = nums[0]
        index = 1
        while(index < len(nums)):
            if(nums[index] == previous):
                del nums[index]
            else:
                previous = nums[index]
                index += 1
        return len(nums)
                

s = Solution()
print(s.removeDuplicates([]))
print(s.removeDuplicates([1]))
print(s.removeDuplicates([1,1,1,1,1,2,2,2,2]))
print(s.removeDuplicates([1,1,1,1,1,2,2,2,2,3,7,7,8,9,9,10]))


