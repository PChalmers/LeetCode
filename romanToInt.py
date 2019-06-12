class Solution:
    def romanToInt(self, s: str) -> int:
        index = 0
        result = 0
        while index < len(s):
            if(s[index] == 'M'):
                result += 1000
                index += 1
            elif(s[index:index+2] == 'CM'):
                result += 900
                index += 2
            elif(s[index] == 'D'):
                result += 500
                index += 1
            elif(s[index:index+2] == 'CD'):
                result += 400
                index += 2
            elif(s[index] == 'C'):
                result += 100
                index += 1
            elif(s[index:index+2] == 'XC'):
                result += 90
                index += 2
            elif(s[index] == 'L'):
                result += 50
                index += 1
            elif(s[index:index+2] == 'XL'):
                result += 40
                index += 2
            elif(s[index] == 'X'):
                result += 10
                index += 1
            elif(s[index:index+2] == 'IX'):
                result += 9
                index += 2
            elif(s[index] == 'V'):
                result += 5
                index += 1
            elif(s[index:index+2] == 'IV'):
                result += 4
                index += 2
            elif(s[index] == 'I'):
                result += 1
                index += 1
            else:
                return 0
        return result
        


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("IV"))
print(s.romanToInt("IX"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
print(s.romanToInt("MMCM"))
print(s.romanToInt("IV"))


