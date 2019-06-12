class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) -1
        for index in range(len(nums)-2,-1,-1):

            if(nums[right] > nums[index]):
                self.swapValues(nums, right, index)
                return
            right = index
        self.reverseListSection(nums, 0, len(nums)-1)

    def reverseListSection(self, nums, start, end):
        for ind in range(start, end//2):
            print('reverseListSection',ind, start,end)
            self.swapValues(nums, end-ind, ind)

    def swapValues(self, nums, right, left):
        temp = nums[right]
        nums[right] = nums[left]
        nums[left] = temp

s = Solution()
l = [1,2,3,4,5,6]
s.nextPermutation(l)
print(l)

l = [1,2,3,4,6,5]
s.nextPermutation(l)
print(l)

l = [6,5,4,3,2]
s.nextPermutation(l)
print(l)
#1,2,3 → 1,3,2
#3,2,1 → 1,2,3
#1,1,5 → 1,5,1
#1,2,3,5,4,6 → 1,2,3,5,6,4