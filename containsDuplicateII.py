class Solution:
    def containsNearbyDuplicate(self, nums, k):
        values = {}

        for index,char in enumerate(nums):
            if(char in values.keys()):
                indexesOfChar = values[char]
                indexesOfChar.append(index)
                if((indexesOfChar[-1] - indexesOfChar[-2]) <= k):
                    return True
                values[char] = indexesOfChar
            else:
                values[char] = [index]
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3))
print(s.containsNearbyDuplicate([1,0,1,1], 1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3],2))