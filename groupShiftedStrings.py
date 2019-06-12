class Solution:
    def groupStrings(self, strings):
        groups = {}
        for string in strings:
            key = ''
            if(len(string) == 0):
                key = 'empty'
            elif(len(string) == 1):
                key = 'oneChar'
            else:
                for index in range(1,len(string)):
                    # Create unique key based on pattern of letters 
                    value = (ord(string[index]) - ord(string[index-1]))
                    if(value > 0):
                        key += 'U' + str(value)
                    elif(value < 0):
                        key += 'U' + str(value + 26)
                    else:
                        key += 'S' + str(value)
                    print('string ', string, 'ord char ', ord(string[index]), 'ord char prev ', ord(string[index-1]), 'value = ', value, 'key = ', key)
            if(key in groups.keys()):
                groups[key].append(string)
            else:
                groups[key] = [string]
            print()
        return list(groups.values())

s = Solution()
print(s.groupStrings(["abc", "bcd", "", "acef", "xyz", "az", "ba", "a", "z", "xa", "yb"]))
