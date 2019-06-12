class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle == ''):
            return 0
        try:
            return haystack.index(needle)
        except:
            return -1


s = Solution()
print(s.strStr('ababa', 'ba'))
print(s.strStr('ababa', 'bac'))
print(s.strStr('ababa', ''))
print(s.strStr('hello', 'll'))