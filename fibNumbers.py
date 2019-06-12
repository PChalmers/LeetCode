class Solution:
    def fib(self, N: int) -> int:
        if(N == 0):
            return 0
        self.values = {0:0,1:1,2:1}
        return self.fibCalc(N)

    def fibCalc(self, num):
        if(num in self.values.keys()):
            return self.values[num]
        self.values[num] = self.fibCalc(num-1) + self.fibCalc(num-2)
        return self.values[num]

s = Solution()
print(s.fib(35))