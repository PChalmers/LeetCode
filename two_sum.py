class Solution:
    def twoSum(self, nums, target):
        for idx1 in range(len(nums)):
            for idx2 in range(idx1+1, len(nums)):
                if(nums[idx1] + nums[idx2] == target):
                    return [idx1, idx2]
        return []

    def twoSum2(self, nums, target):
        temp = {}
        # Get next number from the input list
        for idx in range(len(nums)):
            num = nums[idx]
            # Add the nuxt number to the dict
            temp[idx] = num
            # Find values in dict that can be added to the 
            # current num to total the target
            val = [(key,value) for key, value in temp.items() if value == target-num]
            for (key,value) in val:
                if(key != idx):
                    return sorted([key, idx])
        return []


t = Solution()
print(t.twoSum2([6, 4, 8, 2, 3, 8, 4, 7, 11, 15], target = 9))
print(t.twoSum2([3,2,4,6], target = 6))
print(t.twoSum2([3,2,3], target = 6))

