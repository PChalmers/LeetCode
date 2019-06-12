import itertools

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = numZeros = 0
        try:
            while(True):
                if(nums[index] == 0):
                    del nums[index]
                    numZeros += 1
                else:
                    index += 1
        except:
            pass
        [nums.append(0) for x in range(numZeros)]


nums = [0,0,0,0,0,0,0]
s = Solution()
s.moveZeroes(nums)
print(nums)