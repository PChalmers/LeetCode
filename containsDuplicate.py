class Solution:
    def containsDuplicate(self, nums) -> bool:
        if(len(nums) == len(set(nums))):
            return False
        return True




s = Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))