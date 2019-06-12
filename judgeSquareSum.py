class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 2
        while(start*start < c):
            square = self.isPerfectSquare(c - start*start)
            if(square > 0):
                return start, square
            start +=1
        return start


    def isPerfectSquare(self, num):    
        if(num <= 0):
            return 0
        if(num == 1):
            return 1
        left, right = 0, num 
        while(left < right):
            mid = (left + right) // 2
            if(mid*mid == num):
                return mid
            elif(mid*mid > num):
                right = mid
            else:
                left = mid+1
        return 0


s = Solution()
print(s.judgeSquareSum(29))
print(s.judgeSquareSum(5))
print(s.judgeSquareSum(162))