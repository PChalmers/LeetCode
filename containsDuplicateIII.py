from collections import deque

class Solution:
    def containsNearbyDuplicate(self, nums, k: int, t: int) -> bool:
        numsSeen = deque(maxlen=k)
        for index,char in enumerate(nums):
	        # Look for a number within value range
            for num in range(char - t, char + t + 1):
                if(num in numsSeen):
                    return True
            numsSeen.append(nums[index])
        return False

with open("containsNearbyDuplicateTestcase.txt") as file:
    lines = [line.strip() for line in file]
nums = lines[0].split(',')
nums = [int(x) for x  in nums]

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3, 0))
print(s.containsNearbyDuplicate([1,0,1,1], 1, 2))
print(s.containsNearbyDuplicate([1,5,9,1,5,9], 2, 3))
print(s.containsNearbyDuplicate([2,1], 1, 1))

print(s.containsNearbyDuplicate(nums, int(lines[1]), int(lines[2])))

print(s.containsNearbyDuplicate([0,2147483647], 1, 2147483647))