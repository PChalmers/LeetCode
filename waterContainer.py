class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) -1
        biggest = 0
        while(i<j):
 #           print(i, j, min(height[i], height[j]) * (j-i))
            biggest = max(biggest, min(height[i], height[j]) * (j-i))
            if(height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return biggest

s = Solution()
h = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(h)) # 49
