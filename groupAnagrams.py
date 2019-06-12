class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for string in strs:
            key = ''.join(sorted(string))
            if(key in groups.keys()):
                groups[key].append(string)
            else:
                groups[key] = [string]
        return list(groups.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))