class Solution:
    def largeGroupPositions(self, S: str):
        if(len(S) < 3):
            return []
        results = []
        subString = [S[0], 0, 0, False] # list with latest char and the start and end points in S
        for index in range(len(S)):
            if(S[index] == subString[0]):
                subString[2] = index
                if((subString[2] - subString[1] + 1) >= 3):
                    subString[3] = True
            else:
                if(subString[3]):
                    results.append([subString[1],subString[2]])
                subString = [S[index], index,index, False]
        # check for the last processed char may be a seq
        if(subString[3]):
            results.append([subString[1],subString[2]])
        return results

s = Solution()
print(s.largeGroupPositions("abcdddeeeeaabbbcd")) # [[3,5],[6,9],[12,14]]
print(s.largeGroupPositions("abbxxxxzzy"))
print(s.largeGroupPositions("aaa"))