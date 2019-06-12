class Solution:
    def isValid(self, s: str) -> bool:
        print(s, end=' - ')
        stack = []
        brackets = {')':'(',']':'[','}':'{'}

        for char in s:
            if(char in brackets.values()):
                stack.append(char)
            elif(char in brackets.keys()):
                if(len(stack) == 0):
                    return False
                temp = stack.pop(-1)
                if(temp != brackets[char]):
                    return False
        if(len(stack) != 0):
            return False
        return True


s = Solution()
print(s.isValid("(er)['et']{sd,g}"))
print(s.isValid("([)]"))
print(s.isValid("([{()()}])"))
print(s.isValid(""))
print(s.isValid("]"))