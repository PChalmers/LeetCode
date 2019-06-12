class Solution:
    def removeElement(self, nums, val):
#        print(nums)
        try:
            while(True):
                del nums[nums.index(val)]
        except Exception:
            pass
        
        return len(nums)

s = Solution()
print(s.removeElement([], 3))
print(s.removeElement([3,2,2,3,1,2,3,4,10], 3))
print(s.removeElement([3,3], 3))
print(s.removeElement([3,2,2,3], 3))