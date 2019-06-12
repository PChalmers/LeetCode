class Solution:
    def longestCommonPrefix(self, strs):
        result = ''
        if(len(strs) < 1):
            return result
        for index in range(len(strs[0])):
            char = strs[0][index]
            try:
                for i in strs[1:]:
                    if(i[index] != char):
                        raise Exception
            except:
                return result
            result += char
        return result

s = Solution()
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["fl","fli"]))
print(s.longestCommonPrefix(["fl","fl","fli"]))
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["abecdef","abec","abeced"]))

