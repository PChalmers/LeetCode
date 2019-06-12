class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = {}
        temp = []
        result = ''
        # iterate over string
        for char in s:
            if(not chars.__contains__(char)):
                temp.append(char)
                chars[char] = 1
                if(len(temp) > len(result)):
                    result = ''.join(temp)
            else:
                chars = {char: 1}
                temp = [char]
        return result

    def lengthOfLongestSubstring2(self, s):
        start = end = -1
        result = 0
        chars = {}
        for index, char in enumerate(s):
            # Duplicate found - save the current sequence length if it is longest so far
            if(char in chars):
                result = max(result, end - start)
                start = max(chars[char], start)
            #else:
            end = index
            chars[char] = index
        return max(result, end - start)



s = Solution()

print(s.lengthOfLongestSubstring2("aabaab!bb"))
print(s.lengthOfLongestSubstring2("")) # abc
print(s.lengthOfLongestSubstring2("abcabcbb")) # abc
print(s.lengthOfLongestSubstring2("bbbbbb")) # b
print(s.lengthOfLongestSubstring2("pwwkew")) # wke
print(s.lengthOfLongestSubstring2("dvdf")) # vdf