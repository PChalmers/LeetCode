class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


s = Solution()
print(s.lengthOfLastWord("Hello World"))
print(s.lengthOfLastWord(""))
print(s.lengthOfLastWord("   "))
print(s.lengthOfLastWord("Hello "))
print(s.lengthOfLastWord("Hello"))
print(s.lengthOfLastWord("a "))