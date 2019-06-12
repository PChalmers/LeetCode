class Solution:
    def climbStairs(self, n: int) -> int:
        # n under 3 does not follow the fib series
        if(n < 0): 
            return 0
        if(n <= 2): 
            return n

        # Initiate array for storing values found. Note, only really need the last 2
        # 1 more than n because the value we need is the fib series shifted up by 1
        values = [0]*(n+1) 
        values[0] = 1
        values[1] = 1
        for i in range(2,n+1):
            values[i] = values[i-1] + values[i-2]
        return values[n]


s = Solution()
print(s.climbStairs(35))

