class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for index in range(len(nums)):
            if(nums[index] >= target):
                return index
        return len(nums)
            
s = Solution()
print(s.searchInsert([], 5))
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 3))
print(s.searchInsert([1,3,5,6], 4))
print(s.searchInsert([1,3,5,6], 0))
print(s.searchInsert([1,3,5,6], 7))