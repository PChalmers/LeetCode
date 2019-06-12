class Solution:
    def isPalindrome(self, x: int) -> bool:
        fwd = str(x)
        rev = fwd[::-1]
        for index in range(len(fwd)//2):
            if fwd[index] != rev[index]:
                return False
        return True


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(12131))
print(s.isPalindrome(121234))
print(s.isPalindrome(1221))
