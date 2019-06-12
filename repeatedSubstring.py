class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if(len(s) <= 1):
            return False
        subString = ''
        for i in range(1,len(s)//2+1):
            if(len(s) % i == 0):
                subString = s[0:i]
 #               print(subString)
                result = True
                for index in range(len(subString)):
                    result = result and self.checkForDuplicate(s, s[index], index, i)
                if(result):
                    print(subString)
                    return True
        return False

    # Initial position is location of char to check for duplicstes
    def checkForDuplicate(self, s, char, position, interval):
        newPosition = position+interval
        if(newPosition >= len(s)):
            return True
        if(s[newPosition] != char):
            return False
        return True and self.checkForDuplicate(s, char, newPosition, interval)

s = Solution()
print(s.repeatedSubstringPattern(''))
print(s.repeatedSubstringPattern('ababab'))
print(s.repeatedSubstringPattern('abcde'))
print(s.repeatedSubstringPattern('bbbbbbbb'))
print(s.repeatedSubstringPattern('asdfasdfgasdfasdfg'))
print(s.repeatedSubstringPattern('abcabcyabc'))

