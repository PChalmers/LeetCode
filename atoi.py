class Solution:
    def myAtoi(self, str: str) -> int:
        '''2 states
        0 - initial state
        1 - numbers only
        '''
        state = 0
        parts = list(str)
        result = []

        for char in parts:
            if(state in [0] and char in [' ']):
                pass
            elif(state in [0] and char in ['-', '+'] ):
                result.append(char)
                state = 1
            elif(char in ['0','1','2','3','4','5','6','7','8','9']):
                result.append(char)
                state = 1
            else:
                return self.returnResult(result)
            
        return self.returnResult(result)

    def returnResult(self, l):
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        try:
            # Only return valid integers
            result = int(''.join(l))
            if(result < 0 and abs(result) > 2**31): return INT_MIN
            if(result > 2**31-1): return INT_MAX
            if(result == ''): return 0
            return result
        except:
            return 0

s = Solution()
#print(s.myAtoi(""))
#print(s.myAtoi("  --213"))
#print(s.myAtoi("42"))
#print(s.myAtoi("   -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("+-42"))
print(s.myAtoi("2147483647"))
print(s.myAtoi("2147483648"))
print(s.myAtoi("-2147483648"))
print(s.myAtoi("-2147483649"))
