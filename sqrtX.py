class Solution:
    def mySqrt(self, x: int) -> int:
        if(x <= 0):
            return 0
        if(x == 1):
            return 1
        left, right = 0, x 
        while(left < right):
            mid = (left + right) // 2
            if(mid*mid <= x < (mid+1) * (mid+1)):
                return mid
            elif(mid*mid > x):
                right = mid
            else:
                left = mid+1

s = Solution()
print(s.mySqrt(1))
print(s.mySqrt(2))
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(81))
print(s.mySqrt(1518991037))