class Solution:
    def reverse(self, x: int) -> int:
        ans = int(''.join(reversed(list(str(abs(x))))))
        if(x < 0):
            if(ans > 2**31): return 0
            return ans * -1
        if(ans > 2**31-1): return 0
        return ans

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(-1534236469))
print(s.reverse(1534236469))

# −231,  231 − 1