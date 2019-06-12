import math

class Solution:
    def intToRoman(self, num):
        n = {1:'I',     
            5:'V',      4:'IV',
            10:'X',     9:'IX',
            50:'L',     40:'XL',
            100:'C',    90:'XC',
            500:'D',    400:'CD',
            1000:'M',   900:'CM'}
        orderToCheck = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ''
        for value in orderToCheck:
            t = num // value
            ans += n[value] * t
            num = num - t*value
        return ans

s = Solution()
print(s.intToRoman(3)) # III
print(s.intToRoman(4)) # IV
print(s.intToRoman(9)) # IX
print(s.intToRoman(58)) # LVIII
print(s.intToRoman(1994)) # MCMXCIV