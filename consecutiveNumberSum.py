from datetime import datetime
import math

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        
        # Check for valid input
        if(N <= 2):
            return N
        results = [N]
        # Check for sequences
        for width in range(2, max(int(math.sqrt(N)), int(0.001*N))):
            result =self.sumPossible(N, width)
            if(result != []):
                results.append(result)
        print()
        return len(results)

    def sumPossible(self, targetNum, width):
        height = (targetNum - (width*width - width)/2) / width
        if(height > 0 and height == math.ceil(height)):
                values = [int(height+i) for i in range(0,width)]
                print(width, end=', ') #, values)
                return values
        return []

s = Solution()
print(s.consecutiveNumbersSum(1000))
print(s.consecutiveNumbersSum(1001))
# print(s.consecutiveNumbersSum(9))
# print(s.consecutiveNumbersSum(15))

start = datetime.now()

print(s.consecutiveNumbersSum(1000000000))

end = datetime.now()
elapsed = end - start
print(elapsed)

start = datetime.now()

print(s.consecutiveNumbersSum(1000000001))

end = datetime.now()
elapsed = end - start
print(elapsed)